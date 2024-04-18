"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

directory_operation.py:
=======================
This file contains DirectoryOperation class, responsible to handle directory operations.
Such as: Directory creation.

Guidelines:
===========
Import Statement Guidelines:
============================
Absolute imports are preferred over relative imports for better clarity and consistency.
Built-in Python modules appear first, followed by internal types with a one-line gap,
then external modules and external types, and finally custom modules.

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
from dataclasses import dataclass, field
from os import makedirs

# Include custom packages and modules.
from src.app.utility.handler.log_handler.log_handler import LogHandler


# Define custom directory exception.
# I haven't moved this exception to its separate folder because this,
# exception is only relevant to directory operations.
class DirectoryException(Exception):
    """Class to handle directory errors."""

@dataclass
class DirectoryOperation:
    """Class to handle directory operations, such as directory creation."""

    # Instantiate LogHandler.
    _log_handler: LogHandler = field(default_factory=LogHandler)

    def create_directory(self, directory_path: str) -> None:
        """Create a directory at the specified path if it doesn't already exist.

        Args:
            - directory_path (str): The path where the directory should be created.
                If the directory already exists, no action is taken.

        Returns:
            - None.

        Raises:
            - Exception: if 
        """

        try:
            makedirs(name=directory_path, exist_ok=True)

        except DirectoryException as err:
            self._log_handler.create_log(
                log_type="error",
                log_message=f"A error related to directory operation has occurred. {err}")
