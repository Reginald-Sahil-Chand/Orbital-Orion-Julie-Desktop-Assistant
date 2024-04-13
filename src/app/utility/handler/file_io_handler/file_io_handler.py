"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaning full but follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

file_io_handler.py:
===================
This file contains FileIoHandler class, responsible to handle file operations.

Overview:
=========
This class consists of one contact method named: create_file_operation(arguments).
Returns the file content or none.

Usage:
======
1. Inherit AbstractFileIoHandler and implement the abstract method
to define custom file operation handling behavior.
2. Instantiate the subclass to use the implemented file operation handling functionality.

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
from dataclasses import dataclass, field

# Include custom packages and modules.
from src.app.design_pattern.adapter.abstract.blueprint.abstract_file_io_handler\
    .abstract_file_io_handler import AbstractFileIoHandler
from src.app.utility.handler.log_handler.log_handler import LogHandler


# Define custom csv file exception.
# I haven't moved this exception to its separate folder because this,
# exception only handles csv locally.
class FileTypeWillBeSupportedSoonError(Exception):
    """Class to handle CSV File unsupported error."""


@dataclass
class FileIoHandler(AbstractFileIoHandler):
    """Class to handle create_file_operation instantiation."""

    # Instantiate LogHandler
    log_handler: LogHandler = field(default_factory=LogHandler)

    def create_file_operation(self,
                              file_type: str,
                              file_path: str,
                              file_mode: str,
                              file_contents: (str | dict[str, str])) -> (
                                  (str | dict[str, str] | None)):
        """This method is responsible for creating the file operations.

        File operations in this context are as follows:
            - File Operation [1]: Read file.
            - File Operation [2]: Write file.
            - File Operation [3]: Append file.

        Args:
            - self (Self@AbstractFileIoHandler): Refers to the base class.
            - file_type (str): There are three currently supported file types:
                - File Type [1]: text.
                - File Type [1]: json.
                - File Type [1]: csv. (Support to be added at a later date.)

            - file_path (str): File path refers to the path where the file will be
            created or read from.
                - Note that file_path consists of the following in order:
                    - [1]: File directory.
                    - [2]: File name.
                    - [3]: File extension.
                - Example: src/example.txt

            - file_mode (str): File mode refers to the mode for the file operation.
                - There are three file modes currently supported:
                    - File Mode [1]: "r" => read file.
                    - File Mode [2]: "w" => write file.
                    - File Mode [3]: "a" => append to current existing file.

            - file_contents (str): File contents refer to the content of the file.
                - Here content means when you are creating a file, reading or writing a file,
                what does the file contain, this can be a list of items, block of text or,
                basically anything, just like notes.

        Returns:
            - (str | dict[str, str] | None)
            - We return str (string) => when we are trying to read a file such as a text file.
            - We return dict[str, str] => when we are trying to read a file such as a json file.
            - We return None (Nothing) => when we are trying to create a file.
            - This is because, currently there is no such use case to return a file,
            when creating it.
        """

        # Define file data for file type and file mode checking.
        _file_data = {
            "file_types": {
                "text": "text",
                "json": "json",
                "csv": "csv"
            },

            "file_modes": {
                "read": "r",
                "write": "w",
                "append": "a"
            }
        }

        # Error handling.
        _file_types = list(key for key in _file_data["file_types"])
        _file_modes = list(key for key in _file_data["file_modes"].values())
        _min_file_contents_length = 1

        if file_type not in _file_types:
            raise TypeError(f"The given file type does not match the expected types: {_file_types}")

        if file_type == _file_data["file_types"]["csv"]:
            raise FileTypeWillBeSupportedSoonError(
                "CSV File type will be supported soon. Sorry for the inconvenience caused.")

        if not file_path.strip():
            raise ValueError("Please note that the file path cannot be empty.")

        if file_mode not in _file_modes:
            raise TypeError(f"The given file mode does not match the expected modes: {_file_modes}")

        if isinstance(file_contents, str):
            if not file_contents.strip():
                raise ValueError("Please note that the file contents cannot be empty.")

        if isinstance(file_contents, dict):
            if len(file_contents) < _min_file_contents_length:
                raise ValueError("Please note that the file contents cannot be empty.")

            for key, value in file_contents.items():
                if not key.strip():
                    raise KeyError("Please note that the key cannot be empty.")

                if not value.strip():
                    raise ValueError("Please note that the value cannot be empty.")

        try:
            self.adapter_creates_file(file_type, file_path, file_mode, file_contents)
            print(f"File successfully created at. {file_path}")
            self._log_handler.create_log(
                log_type="info",
                log_message=f"File successfully created at. {file_path}")

        except FileNotFoundError as err:
            self._log_handler.create_log(
                log_type="error",
                log_message=f"File not found. Possible missing directory. {err}")
