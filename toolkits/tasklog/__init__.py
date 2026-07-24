"""
TaskLog - Daily Task Execution Tracker

A lightweight package for managing daily task execution status and preventing duplicate runs.
Automatically retries failed tasks.

Features:
---------
- Automatic skip for successfully executed tasks
- Auto retry for failed tasks
- Persistent JSON-based storage
- Easy management and monitoring

Usage:
------
from tasklog import daily_run, operate, show_records

# Method 1: Decorator (Recommended)
@daily_run()
def my_task():
    print("Executing task...")
    return result

# Method 2: Function wrapper
def another_task():
    return data

result = operate(another_task, name='data_processing')

# View execution records
show_records()
show_records(show_failed_only=True)  # Show only failed tasks

# Check status
from tasklog import is_updated_today
if not is_updated_today('my_task'):
    print("Task needs to run")

# Manage records
from tasklog import reset_record, clear_old_records
reset_record('my_task')  # Reset specific task
clear_old_records(days=30)  # Clean old records
"""

from .tracker import (
    # Core functions
    operate,
    daily_run,
    daily_run_with_params,
    
    # Query functions
    is_updated_today,
    get_record,
    get_failed_tasks,
    
    # Display functions
    show_records,
    
    # Management functions
    update_record,
    reset_record,
    reset_all_records,
    reset_failed_records,
    clear_old_records,
)

from .utils import (
    # Utility functions
    load_records,
    save_records,
    ensure_record_file,
    set_record_file,
)

__version__ = '1.0.0'
__author__ = 'Your Name'
__all__ = [
    # Core execution
    'operate',
    'daily_run',
    'daily_run_with_params',
    
    # Status queries
    'is_updated_today',
    'get_record',
    'get_failed_tasks',
    
    # Display
    'show_records',
    
    # Record management
    'update_record',
    'reset_record',
    'reset_all_records',
    'reset_failed_records',
    'clear_old_records',
    
    # Utilities
    'load_records',
    'save_records',
    'ensure_record_file',
    'set_record_file',
]
