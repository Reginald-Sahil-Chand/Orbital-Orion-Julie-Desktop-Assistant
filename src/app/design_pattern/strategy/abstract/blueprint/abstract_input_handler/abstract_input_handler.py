"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaning full but follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

abstract_input_handler.py:
========================
Acts as a blueprint for the input_handler utility class.
This class houses only one method that the input_handler must implement before instantiation.

Overview:
=========
This class consists of one abstract method named:
create_input(input_type: str, input_display_message: str = ""):
Returns the input value.

Usage:
======
1. Inherit AbstractInputHandler and implement the abstract method to define custom input type
handling behavior.
2. Instantiate the subclass to use the implemented input handling functionality.

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
class AbstractInputHandler(ABC):
    """An abstract base class for handling input utility functions."""

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
