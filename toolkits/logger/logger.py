'''
Author: Qimin Ma
Date: 2026-03-13 20:48:20
LastEditTime: 2026-03-13 20:48:24
FilePath: /Toolkit/logger/logger.py
Description:
Copyright (c) 2026 by Qimin Ma, All Rights Reserved.
'''
from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING, Any, Callable, Optional

from dotenv import load_dotenv
from loguru import logger as loguru_logger

if TYPE_CHECKING:
    from loguru import Logger

load_dotenv()

DEFAULT_LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
DEFAULT_LOGGER_DIR = os.environ.get("LOGGER_DIR", "./logs")

# Bound logger messages are filtered by this extra key (same semantics as unique logging.Logger name).
_EXTRA_KEY = "_toolkit_logger_name"

_CONFIGURED_NAMES: set[str] = set()
_DEFAULT_HANDLER_REMOVED = False
_FILE_SINK_IDS: dict[str, int] = {}


def _remove_default_handler_once() -> None:
    """Loguru ships with a default stderr sink; remove it once so only our sinks run."""
    global _DEFAULT_HANDLER_REMOVED
    if not _DEFAULT_HANDLER_REMOVED:
        loguru_logger.remove()
        _DEFAULT_HANDLER_REMOVED = True


def _make_filter(name: str) -> Callable[[Any], bool]:
    def _filter(record: Any) -> bool:
        return record["extra"].get(_EXTRA_KEY) == name

    return _filter


def get_logger(
    name: str = "smart_dataloader",
    filename: Optional[str] = None,
    level: Optional[str] = None,
    ifconsole: bool = True,
) -> "Logger":
    """Return a configured Loguru logger. Optionally log to console and/or a file.

    Same behavior as before: sinks are attached only the first time each ``name`` is
    seen (subsequent calls with the same ``name`` ignore new ``filename`` / options).

    Args:
        name: Logical logger name (used for filtering and display).
        filename: If set, also write to ``{LOGGER_DIR}/{filename}.log``. If ``None``, no file output.
        level: Log level (e.g. ``DEBUG``, ``INFO``). Uses ``LOG_LEVEL`` env if not set.
        ifconsole: If ``True``, add a colored stderr sink.

    Returns:
        A Loguru ``Logger`` (bound) with ``.info()``, ``.warning()``, ``.error()``, etc.
    """
    level_str = (level or DEFAULT_LOG_LEVEL).upper()

    if name not in _CONFIGURED_NAMES:
        _remove_default_handler_once()

        fmt_console = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{extra[_toolkit_logger_name]}</cyan> | "
            "<level>{message}</level>"
        )
        fmt_file = (
            "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | "
            "{extra[_toolkit_logger_name]} | {message}\n"
        )

        if ifconsole:
            loguru_logger.add(
                sys.stderr,
                format=fmt_console,
                level=level_str,
                filter=_make_filter(name),
                colorize=True,
            )
        if filename is not None:
            os.makedirs(DEFAULT_LOGGER_DIR, exist_ok=True)
            path = os.path.join(DEFAULT_LOGGER_DIR, f"{filename}.log")
            sink_id = loguru_logger.add(
                path,
                encoding="utf-8",
                format=fmt_file,
                level=level_str,
                filter=_make_filter(name),
            )
            _FILE_SINK_IDS[filename] = sink_id

        _CONFIGURED_NAMES.add(name)

    return loguru_logger.bind(**{_EXTRA_KEY: name})


def delete_logger_file(filename: str = "smart_dataloader") -> None:
    """Remove the log file and its Loguru file sink (Windows-safe: sink removed first)."""
    sink_id = _FILE_SINK_IDS.pop(filename, None)
    if sink_id is not None:
        try:
            loguru_logger.remove(sink_id)
        except ValueError:
            pass
    path = os.path.join(DEFAULT_LOGGER_DIR, f"{filename}.log")
    if os.path.exists(path):
        os.remove(path)
