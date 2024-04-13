"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaning full but follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

file_operation_dataset.py:
==========================
Contains information in a form of dictionary data related to file operations.
Examples include: default file information such as file name, extensions etc.

Usage:
======
This module consists of one function named create_file_operation_data.
This function returns some data that is of type dict. aka returns data in form of a dictionary.
As mentioned earlier, this some data is referred to as the data for the file operations.

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

def create_file_operation_data() -> dict[str, dict[str, str]]:
    """Creates file operation data.
    
    Returns dict[str, dict[str, str]] -> File operation data.
    """

    created_file_operation_data: dict[str, dict[str, str]] = {
        "file_operations": {
            "read": "r",
            "write": "w",
            "append": "a"
        },

        "default_file_information": {
            "directory": "src",
            "name":"default",
            "extension": ".txt",
            "encoding": "UTF-8",
            "contents": "This is a default message since no custom parameters where provided."

        },

        "file_types": {
            "text_file": "txt",
            "json_file": "json",
            "csv_file": "csv"
        },

        "file_extensions": {
            "txt": ".txt",
            "json": ".json",
            "csv": ".csv"
        }
    }

    return created_file_operation_data
