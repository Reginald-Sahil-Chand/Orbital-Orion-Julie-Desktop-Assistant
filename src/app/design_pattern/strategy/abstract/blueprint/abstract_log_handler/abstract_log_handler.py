"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaning full but follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

abstract_log_handler.py:
========================
Acts as a blueprint for the log_handler utility class.

Guidelines:
===========
Import Statement Guidelines:
============================
Absolute imports are preferred over relative imports for better clarity and consistency.
Built-in Python modules appear first, followed by external modules with a one-line gap,
then internal and external types, and finally custom modules.

Usage Notes:
============
Ensure to follow PEP 8 guidelines for import statements.
Use absolute imports to avoid potential naming conflicts.
Keep the import section organized for better readability and maintenance.

Dependencies:
=============
Some modules may have dependencies on external libraries.
Refer to the module documentation for details.
"""

# Include built-in packages and modules.
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AbstractLogHandler(ABC):
    """An abstract base class for handling logging utility functions."""

    @abstractmethod
    def create_log(self, log_type: str, log_message: str = "Log message is undefined.") -> None:
        """Create a log with the given log type and log message.
        
        Args:
        - log_type: (str) -> The type of log required to create a log.
        - Example: error, warning or info.
        - log_message: (str) -> The message required to tell more about the log.
        - Default Log Message: Log message is undefined.
        
        Returns: None
        """
