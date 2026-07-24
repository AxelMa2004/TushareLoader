"""
Timer module for measuring code execution time with configurable units and context manager support.
"""

import time
from typing import Optional, Literal

# Supported time units and their scale relative to seconds
TIME_UNIT_SCALE = {
    "ns": 1e9,
    "us": 1e6,
    "ms": 1e3,
    "s": 1.0,
}

TimeUnit = Literal["ns", "us", "ms", "s"]


class Timer:
    """
    A timer that measures elapsed time with configurable units (default: milliseconds).
    Supports context manager usage and optional custom output message.
    """

    def __init__(
        self,
        unit: TimeUnit = "ms",
        message: Optional[str] = None,
        precision: int = 2,
    ) -> None:
        """
        Initialize the timer.

        Args:
            unit: Time unit for display and elapsed value. One of 'ns', 'us', 'ms', 's'.
            message: Optional text to print before the elapsed time (e.g. "加载数据" -> "加载数据 ... 123.45 ms").
            precision: Number of decimal places for the elapsed value in output.
        """
        if unit not in TIME_UNIT_SCALE:
            raise ValueError(
                f"unit must be one of {list(TIME_UNIT_SCALE.keys())}, got {unit!r}"
            )
        self._unit = unit
        self._message = message
        self._precision = precision
        self._start_time: Optional[float] = None
        self._elapsed_seconds: Optional[float] = None

    def __enter__(self) -> "Timer":
        """Start the timer when entering the context."""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Stop the timer and print elapsed time when exiting the context."""
        self.stop()
        self._print_elapsed()
        return None

    def start(self) -> "Timer":
        """Start the timer. Returns self for chaining."""
        self._start_time = time.perf_counter()
        self._elapsed_seconds = None
        return self

    def stop(self) -> "Timer":
        """Stop the timer and record elapsed time. Returns self for chaining."""
        if self._start_time is None:
            raise RuntimeError("Timer was not started; call start() or use 'with' first.")
        self._elapsed_seconds = time.perf_counter() - self._start_time
        return self

    def elapsed(self, unit: Optional[TimeUnit] = None) -> float:
        """
        Return elapsed time in the given unit (default: the timer's unit).

        Args:
            unit: Override unit for this call. If None, uses the timer's unit.

        Returns:
            Elapsed time in the requested unit.

        Raises:
            RuntimeError: If the timer has not been stopped (no elapsed time yet).
        """
        if self._elapsed_seconds is None:
            raise RuntimeError(
                "No elapsed time yet; call stop() or use context manager to completion."
            )
        u = unit if unit is not None else self._unit
        if u not in TIME_UNIT_SCALE:
            raise ValueError(
                f"unit must be one of {list(TIME_UNIT_SCALE.keys())}, got {u!r}"
            )
        return self._elapsed_seconds * TIME_UNIT_SCALE[u]

    def _print_elapsed(self) -> None:
        """Print elapsed time, with optional message prefix."""
        try:
            value = self.elapsed()
        except RuntimeError:
            return
        unit_label = self._unit
        if self._message:
            print(f"{self._message} ... {value:.{self._precision}f} {unit_label}")
        else:
            print(f"... {value:.{self._precision}f} {unit_label}")