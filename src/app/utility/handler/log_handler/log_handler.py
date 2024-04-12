"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaning full but follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

log_handler.py:
===============
The log_handler utility class.
This class houses one method that the log_handler must implement before instantiation.

Overview:
=========
This class consists of one method named:
create_log(log_type: str, log_message: str = "Log message is undefined."):
Creates a log with the given message. (This method represents the abstract method).

Usage:
======
1. Inherit AbstractLogHandler and implement the abstract method to define custom log
handling behavior.
2. Instantiate the subclass to use the implemented log handling functionality.

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
from dataclasses import dataclass
from logging import basicConfig, error, warning, info, DEBUG

from src.app.design_pattern.strategy.abstract.blueprint.abstract_log_handler\
    .abstract_log_handler import AbstractLogHandler


@dataclass
class LogHandler(AbstractLogHandler):
    """A logger class inheriting AbstractLogHandler abstract class for handling logging
    utility functions.
    """

    basicConfig(format="%(levelname)s: %(message)s", level=DEBUG)

    _log_type_error: str = "error"
    _log_type_warning: str = "warning"
    _log_type_info: str = "info"

    def create_log(self, log_type: str, log_message: str = "Log message is undefined.") -> None:
        """Create a log with the given log type and log message.
        
        Args:
        - log_type: (str) -> The type of log required to create a log.
        - Example: error, warning or info.
        - log_message: (str) -> The message required to tell more about the log.
        - Default Log Message: Log message is undefined.
        
        Returns: None
        """

        try:
            if not log_message.strip():
                error(msg="Log message cannot be empty.")
                raise ValueError("Log message cannot be empty.")

            match log_type:
                case self._log_type_error:
                    error(msg=log_message)

                case self._log_type_warning:
                    warning(msg=log_message)

                case self._log_type_info:
                    info(msg=log_message)

                case _:
                    error(msg="The provided type does not meet the required log_type")
                    raise TypeError(
                            "The provided type does not meet the required log_type: ",
                            f"{self._log_type_error}, or {self._log_type_warning}, "
                            f"or {self._log_type_info}")

        except ValueError:
            error(msg="Please re-check your \"log_message\" parameter.")
