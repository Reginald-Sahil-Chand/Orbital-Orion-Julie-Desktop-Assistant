"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

input_handler.py:
=================
This file contains InputHandler class, responsible to handle user inputs.

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

# Include internal typings.
from typing import Dict, Tuple

# Include custom packages and modules.
from src.app.design_pattern.strategy.abstract.blueprint.abstract_input_handler\
    .abstract_input_handler import AbstractInputHandler
from src.app.utility.handler.log_handler.log_handler import LogHandler


@dataclass
class InputHandler(AbstractInputHandler):
    """A input class inheriting AbstractInputHandler abstract class for handling user inputs."""

    # Instantiate LogHandler.
    _log_handler: LogHandler = field(default_factory=LogHandler)

    _available_input_types: Dict[str, type] = field(default_factory=lambda: {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool
    })

    _store_available_input_types: Tuple[str, ...] = ()

    # You can also import and use the Union type. (Both does the same thing).
    _store_input_value: (str | int | float | bool) = ""

    _input_type_mismatch_error_message: str = ""

    _input_value: str = ""

    # Use post init, other wise the interpreter will not know if the object is initialized.
    # It is used to actually populate the _available_input_types keys in
    # _store_available_input_types after InputHandler class initialization.
    # * We need to use __post_init__ to inform filed that the class is now initialized,
    # * Hence return the values.
    def __post_init__(self):
        self._store_available_input_types: Tuple[str, ...] = (
            tuple(self._available_input_types.keys()))

        self._input_type_mismatch_error_message = (
        f"Alert! Type Mismatch. Allowed types are: {self._store_available_input_types}")

    def create_input(self, input_type: str,
                     input_display_message: str = "") ->  (str | int| float | bool | None):
        """Create a input with the given input type and an optional input display message.
        
        Args:
        - input_type (str): The input type required to create a user input.
        - input_display_message (str): The message for the user to know what to enter,
        in the input field.
        
        Returns:
            - (str | int | float | bool | None): User's entered input value or none.

        Raises:
            - Exception: if user's entered input value is empty.
        """

        try:
            if not input_type.strip():
                self._log_handler.create_log(
                    log_type="error",
                    log_message="Please note that the input type cannot be empty.")

                raise ValueError("Please note that the input type cannot be empty.")

            if input_type not in self._available_input_types:
                self._log_handler.create_log(
                    log_type="error",
                    log_message=self._input_type_mismatch_error_message)

                raise TypeError(self._input_type_mismatch_error_message)

            # Ask the user to enter an input
            self._input_value = input(input_display_message)

            # Check if the input type equals the available input types,
            # And convert the inputs respectively.
            for index, _ in enumerate(self._store_available_input_types):
                if self._store_available_input_types[index] == input_type:
                    self._store_input_value = (
                        self._available_input_types[input_type](self._input_value))

            return self._store_input_value

        except ValueError:
            self._log_handler.create_log(
                    log_type="error",
                    log_message="Alert! provided input value is invalid.")

            return None
