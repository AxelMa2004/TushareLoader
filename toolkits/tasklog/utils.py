"""Utility functions"""

import json
import os
from pathlib import Path

# Default configuration
DEFAULT_RECORD_FILE = os.path.join(
    os.path.dirname(__file__), 
    'record.json'
)

# Allow users to customize record file path via environment variable
RECORD_FILE = os.environ.get('TASKLOG_RECORD_FILE', DEFAULT_RECORD_FILE)

def ensure_record_file():
    """Ensure record file exists"""
    record_path = Path(RECORD_FILE)
    record_path.parent.mkdir(parents=True, exist_ok=True)
    
    if not record_path.exists():
        with open(record_path, 'w', encoding='utf-8') as f:
            json.dump({}, f)

def load_records():
    """Load execution records from JSON file"""
    ensure_record_file()
    try:
        with open(RECORD_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Return empty dict if file is corrupted
        return {}

def save_records(records):
    """Save execution records to JSON file"""
    ensure_record_file()
    with open(RECORD_FILE, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def set_record_file(path):
    """
    Set custom record file path
    
    Parameters:
    -----------
    path : str
        Path to the record file
    """
    global RECORD_FILE
    RECORD_FILE = path
    ensure_record_file()
