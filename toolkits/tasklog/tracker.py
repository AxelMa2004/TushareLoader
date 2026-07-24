"""Core tracking functionality"""

import datetime
from functools import wraps
from .utils import (
    load_records,
    save_records,
    ensure_record_file,
)

def update_record(name, status='success', extra_info=None):
    """Update execution record for a function"""
    records = load_records()
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    
    records[name] = {
        'date': today,
        'status': status,
        'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'extra_info': extra_info
    }
    
    save_records(records)

def is_updated_today(name):
    """
    Check if a function has been successfully executed today
    
    Note: Only 'success' status counts as executed
    If last execution failed, returns False even if it was today
    """
    records = load_records()
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    
    if name not in records:
        return False
    
    record = records[name]
    
    # Must satisfy both: date is today AND status is success
    return record.get('date') == today and record.get('status') == 'success'

def get_record(name):
    """Get execution record for a function"""
    records = load_records()
    return records.get(name)

def operate(func, name=None, force=False, logger=None, **kwargs):
    """
    Execute function and record execution status
    
    Parameters:
    -----------
    func : callable
        Function to execute
    name : str, optional
        Function name, defaults to func.__name__
    force : bool, default False
        Whether to force execution (ignore today's record)
    logger : logging.Logger, optional
        Logger instance to use for output, defaults to None (print to console)
    **kwargs : dict
        Parameters to pass to func
    
    Returns:
    --------
    result : any
        Function execution result, None if skipped
        
    Notes:
    ------
    - Skips if successfully executed today
    - Re-executes if failed today
    """
    if name is None:
        name = func.__name__
    
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    
    # Check if execution is needed
    if not force and is_updated_today(name):
        msg = f"⏭️  Skip [{name}]: Already executed successfully today ({today})"
        if logger:
            logger.info(msg)
        else:
            print(msg)
        return None
    
    # Check if this is a retry after failure
    record = get_record(name)
    if record and record.get('date') == today and record.get('status') == 'failed':
        msg = f"🔄 Retry [{name}]: Last execution failed, re-running..."
        if logger:
            logger.info(msg)
        else:
            print(msg)
    else:
        msg = f"🚀 Start executing [{name}]..."
        if logger:
            logger.info(msg)
        else:
            print(msg)
    
    # Execute function
    try:
        result = func(**kwargs)
        update_record(name, status='success', extra_info={'result_type': type(result).__name__})
        msg = f"✅ [{name}] Execution successful, recorded to {today}"
        if logger:
            logger.info(msg)
        else:
            print(msg)
        return result
    
    except Exception as e:
        update_record(name, status='failed', extra_info={'error': str(e)})
        msg = f"❌ [{name}] Execution failed: {e}"
        if logger:
            logger.error(msg)
        else:
            print(msg)
        raise

def daily_run(name=None, force=False, logger=None):
    """
    Decorator: Automatically manage daily execution status of functions
    
    Usage:
    ------
    @daily_run()
    def my_function():
        pass
    
    @daily_run(name='custom_name', force=True, logger=my_logger)
    def another_function():
        pass
        
    Notes:
    ------
    - Skips if successfully executed today
    - Automatically retries if failed today
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = name if name else func.__name__
            today = datetime.datetime.today().strftime("%Y-%m-%d")
            
            # Check if execution is needed
            if not force and is_updated_today(func_name):
                msg = f"⏭️  Skip [{func_name}]: Already executed successfully today ({today})"
                if logger:
                    logger.info(msg)
                else:
                    print(msg)
                return None
            
            # Check if this is a retry after failure
            record = get_record(func_name)
            if record and record.get('date') == today and record.get('status') == 'failed':
                msg = f"🔄 Retry [{func_name}]: Last execution failed, re-running..."
                if logger:
                    logger.info(msg)
                else:
                    print(msg)
            else:
                msg = f"🚀 Start executing [{func_name}]..."
                if logger:
                    logger.info(msg)
                else:
                    print(msg)
            
            # Execute function
            try:
                result = func(*args, **kwargs)
                update_record(func_name, status='success', 
                            extra_info={'result_type': type(result).__name__})
                msg = f"✅ [{func_name}] Execution successful, recorded to {today}"
                if logger:
                    logger.info(msg)
                else:
                    print(msg)
                return result
            
            except Exception as e:
                update_record(func_name, status='failed', 
                            extra_info={'error': str(e)})
                msg = f"❌ [{func_name}] Execution failed: {e}"
                if logger:
                    logger.error(msg)
                else:
                    print(msg)
                raise
        
        return wrapper
    return decorator

def daily_run_with_params(name=None, force=False, cache_params=True, logger=None):
    """Decorator with parameter caching support"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = name if name else func.__name__
            
            # If parameter caching is enabled, add parameters to name
            if cache_params and (args or kwargs):
                import hashlib
                param_str = f"{args}_{kwargs}"
                param_hash = hashlib.md5(param_str.encode()).hexdigest()[:8]
                func_name = f"{func_name}_{param_hash}"
            
            today = datetime.datetime.today().strftime("%Y-%m-%d")
            
            if not force and is_updated_today(func_name):
                msg = f"⏭️  Skip [{func_name}]: Already executed successfully today"
                if logger:
                    logger.info(msg)
                else:
                    print(msg)
                return None
            
            # Check if this is a retry after failure
            record = get_record(func_name)
            if record and record.get('date') == today and record.get('status') == 'failed':
                msg = f"🔄 Retry [{func_name}]: Last execution failed, re-running..."
                if logger:
                    logger.info(msg)
                else:
                    print(msg)
            else:
                msg = f"🚀 Start executing [{func_name}]..."
                if logger:
                    logger.info(msg)
                else:
                    print(msg)
            
            try:
                result = func(*args, **kwargs)
                update_record(func_name, status='success')
                msg = f"✅ [{func_name}] Execution successful"
                if logger:
                    logger.info(msg)
                else:
                    print(msg)
                return result
            except Exception as e:
                update_record(func_name, status='failed', extra_info={'error': str(e)})
                msg = f"❌ [{func_name}] Execution failed: {e}"
                if logger:
                    logger.error(msg)
                else:
                    print(msg)
                raise
        
        return wrapper
    return decorator

def show_records(show_failed_only=False, logger=None):
    """
    Display all execution records
    
    Parameters:
    -----------
    show_failed_only : bool, default False
        Whether to show only failed records
    logger : logging.Logger, optional
        Logger instance to use for output, defaults to None (print to console)
    """
    records = load_records()
    if not records:
        msg = "📭 No execution records"
        if logger:
            logger.info(msg)
        else:
            print(msg)
        return
    
    if show_failed_only:
        records = {k: v for k, v in records.items() if v.get('status') == 'failed'}
        if not records:
            msg = "✅ No failed records"
            if logger:
                logger.info(msg)
            else:
                print(msg)
            return
    
    # Prepare output lines for better log readability
    lines = []
    lines.append("\n📊 Execution Records:")
    lines.append("-" * 90)
    lines.append(f"{'Status':^6} {'Task Name':^30} {'Date':^12} {'Update Time':^20} {'Note':^15}")
    lines.append("-" * 90)
    
    for name, info in records.items():
        status_icon = "✅" if info['status'] == 'success' else "❌"
        extra = ""
        if info['status'] == 'failed' and info.get('extra_info', {}).get('error'):
            error = info['extra_info']['error']
            extra = error[:15] + "..." if len(error) > 15 else error
        
        lines.append(f"{status_icon:^6} {name:30s} {info['date']:12s} {info['update_time']:20s} {extra:15s}")
    
    lines.append("-" * 90)
    
    # Statistics
    total = len(records)
    success = sum(1 for v in records.values() if v['status'] == 'success')
    failed = total - success
    lines.append(f"\nTotal: {total} | Success: {success} | Failed: {failed}")
    
    # Output all content
    full_msg = "\n".join(lines)
    if logger:
        logger.info(full_msg)
    else:
        print(full_msg)

def get_failed_tasks(today_only=True):
    """
    Get list of failed tasks
    
    Parameters:
    -----------
    today_only : bool, default True
        Whether to return only today's failed tasks
    
    Returns:
    --------
    list : List of failed task names
    """
    records = load_records()
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    
    failed = []
    for name, info in records.items():
        if info.get('status') == 'failed':
            if today_only:
                if info.get('date') == today:
                    failed.append(name)
            else:
                failed.append(name)
    
    return failed

def clear_old_records(days=30, logger=None):
    """Clear records older than N days"""
    records = load_records()
    today = datetime.datetime.today()
    cutoff = (today - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    
    new_records = {
        name: info for name, info in records.items()
        if info['date'] >= cutoff
    }
    
    removed = len(records) - len(new_records)
    save_records(new_records)
    msg = f"🗑️  Cleared {removed} records older than {days} days"
    if logger:
        logger.info(msg)
    else:
        print(msg)
    return removed

def reset_record(name, logger=None):
    """Reset record for a function (will re-execute next time)"""
    records = load_records()
    if name in records:
        del records[name]
        save_records(records)
        msg = f"🔄 Reset record for [{name}]"
        if logger:
            logger.info(msg)
        else:
            print(msg)
        return True
    else:
        msg = f"⚠️  Record not found for [{name}]"
        if logger:
            logger.warning(msg)
        else:
            print(msg)
        return False

def reset_all_records(logger=None):
    """Reset all records"""
    save_records({})
    msg = "🔄 Reset all records"
    if logger:
        logger.info(msg)
    else:
        print(msg)

def reset_failed_records(logger=None):
    """Reset all failed records"""
    records = load_records()
    failed_tasks = [name for name, info in records.items() if info.get('status') == 'failed']
    
    for name in failed_tasks:
        del records[name]
    
    save_records(records)
    msg = f"🔄 Reset {len(failed_tasks)} failed records: {failed_tasks}"
    if logger:
        logger.info(msg)
    else:
        print(msg)
    return failed_tasks