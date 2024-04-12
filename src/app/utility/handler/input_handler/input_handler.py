"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaning full but follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

input_handler.py:
=================
The input_handler utility class.
This class houses only one method that the input_handler must implement before instantiation.

Overview:
=========
This class consists of one method named:
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
from dataclasses import dataclass

# Include custom packages and modules.
from src.app.design_pattern.strategy.abstract.blueprint.abstract_input_handler\
    .abstract_input_handler import AbstractInputHandler
from src.app.utility.handler.log_handler.log_handler import LogHandler


@dataclass
class InputHandler(AbstractInputHandler):
    """A input class inheriting AbstractInputHandler abstract class for handling user inputs."""

    # Instantiate LogHandler.
    log_handler = LogHandler()

    available_input_types = {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool
    }

    store_available_input_types = set(available_input_types)

    # You can also import and use the Union type. (Both does the same thing).
    input_value: (str | int | float | bool) = ""

    def create_input(self, input_type: str,
                     input_display_message: str = "") ->  (str | int| float | bool | None):
        """Create a log with the given log type and log message.
        
        Args:
        - input_type: (str) -> The input type required to create a user input.
        - input_display_message: (str) -> The message for the user to know what to enter,
        in the input field.
        
        Returns: (str | int| float | bool | None)
        """

        try:
            if not input_type.strip():
                self.log_handler.create_log(
                    log_type="error",
                    log_message=f"Input type cannot be empty.\n"
                    f"Allowed input types: {self.store_available_input_types}")

                raise ValueError(
                    f"Input type cannot be empty.\n"
                    f"Allowed input types: {self.store_available_input_types}")

            input_converter: type[str] | type[int] | type[float] | type[bool] | None = (
                self.available_input_types.get(input_type))

            if input_converter is None:
                raise TypeError(
                    f"Invalid input type: {input_type}\n"
                    f"Allowed input types: {self.store_available_input_types}")

            self.input_value = input_converter(input(input_display_message))
            return self.input_value

        except ValueError:
            return "No valid input identified."
