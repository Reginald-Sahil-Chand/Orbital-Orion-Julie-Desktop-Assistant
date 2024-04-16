"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

custom_value_and_type_validation.py:
====================================
This file contains various error helper modules, responsible to handle various
value and type errors based on the required parameters.

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

def validate_if_value_is_empty(value: str) -> None:
    """Validates if a given value is empty (contains only whitespace characters).

    Args:
        value (str): The value to be validated.

    Raises:
        ValueError: If the value is empty.
    """

    if not value.strip():
        raise ValueError(f"Please note that {value} cannot be empty.")

def validate_if_type_does_not_match(given_type: str, supported_types: list[str]) -> None:
    """Validates if a given type matches the expected types.

    Args:
        given_type (str): The type to be validated.
        supported_types (list[str]): List of supported types.

    Raises:
        TypeError: If the given type does not match the expected types.
    """

    if given_type not in supported_types:
        raise TypeError(
            f"Type {given_type} does not match the expected types: {supported_types}")

def validate_file_contents(file_contents: str | (str | dict[str, str]),
                           min_file_contents_length: int) -> None:
    """Validates file contents based on their type and length.

    Args:
        file_contents (str | dict[str, str]): The file contents to be validated.
        min_file_contents_length (int): Minimum allowed length for file contents.

    Raises:
        ValueError: If the file contents are empty or do not meet the minimum length requirement.
        KeyError: If a key in the file contents dictionary is empty.
    """

    if isinstance(file_contents, str) and not file_contents.strip():
        raise ValueError("Please note that the file contents cannot be empty.")

    if isinstance(file_contents, dict) and len(file_contents):
        if len(file_contents) < min_file_contents_length:
            raise ValueError("Please note that the file contents cannot be empty.")

        for key, value in file_contents.items():
            if not key.strip():
                raise ValueError(f"Please note that {key} cannot be empty.")

            if not value.strip():
                raise ValueError(f"Please note that the {value} cannot be empty.")
