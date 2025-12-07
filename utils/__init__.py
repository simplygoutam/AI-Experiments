"""
Utility Functions Module

Shared utilities and helper functions for AI experiments.
"""

__version__ = "0.1.0"

def log_message(message: str, level: str = "INFO") -> None:
    """
    Log a message with a given level.
    
    Args:
        message: The message to log
        level: Log level (INFO, DEBUG, ERROR)
    """
    print(f"[{level}] {message}")


__all__ = ["log_message"]
