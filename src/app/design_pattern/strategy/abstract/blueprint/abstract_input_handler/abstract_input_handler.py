"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

abstract_input_handler.py:
==========================
Acts as a blueprint for the input_handler utility class.

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
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AbstractInputHandler(ABC):
    """An abstract base class for handling user input."""

    @abstractmethod
    def create_input(self, input_type: str,
                     input_display_message: str = "") -> (str | int| float | bool | None):
        """Create a input with the given input type and input display message.

        Args:
        - input_type: (str) -> The input type required to create a user input.
        - input_display_message: (str) -> The message for the user to know what to enter,
        in the input field.
        
        Returns: (str | int| float | bool | None)
        """
