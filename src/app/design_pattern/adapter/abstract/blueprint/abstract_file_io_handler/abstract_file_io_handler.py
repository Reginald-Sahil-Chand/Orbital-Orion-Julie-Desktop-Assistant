"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaning full but follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

abstract_file_io_handler.py:
===================================
Acts as a blueprint for the file_handler utility class.

Overview:
=========
This class consists of one abstract method named: create_file_operation(arguments).
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
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import IO, Any
from json import JSONDecodeError, load, dumps

# Include custom packages and modules.
from src.app.utility.handler.log_handler.log_handler import LogHandler


@dataclass
class AbstractFileIoHandler(ABC):
    """An abstract base class for handling file operations."""

    # Instantiate LogHandler.
    _log_handler:LogHandler = field(default_factory=LogHandler)

    # Define file types.
    _file_type_text: str = "text"
    _file_type_json: str = "json"
    _file_type_csv: str = "csv"

    # Define file modes.
    _file_mode_read: str = "r"
    _file_mode_write: str = "w"
    _file_mode_append: str = "a"

    @abstractmethod
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

    def _file_operator(
            self,
            file_type: str,
            file_mode: str,
            file: IO[Any],
            file_contents: (str | dict[str, str])) -> (str | dict[str, str] | None):
        """This method works as a file operator.

        - file_type (str): There are three currently supported file types:
                - File Type [1]: text.
                - File Type [1]: json.
                - File Type [1]: csv. (Support to be added at a later date.)
        
        File operations in this context are as follows:
            - File Operation [1]: File mode (get file mode: r, w, a).
                - Where r => read file.
                - Where w => write file.
                - Where a => append to file.

            - File Operation [2]: File IO (get the file input and output functionality).
            - File Operation [3]: File contents (get the file data).

        Args:
            - self (Self@AbstractFileIoHandler): Refers to the base class.
            - file_mode (str): File mode refers to the mode for the file operation.
                - There are three file modes currently supported:
                    - File Mode [1]: "r" => read file.
                    - File Mode [2]: "w" => write file.
                    - File Mode [3]: "a" => append to current existing file.

            - file (IO[Any]): This refers to the file stream which is being used to perform,
            file operations.

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

        try:
            match file_mode:
                case self._file_mode_read:
                    if file_type == self._file_type_text:
                        file_contents = file.read()
                        return file_contents

                    if file_type == self._file_type_json:
                        file_contents = load(file)
                        return file_contents

                case self._file_mode_write:
                    if file_type == self._file_type_text:
                        file.writelines(file_contents)

                    if file_type == self._file_type_json:
                        json_object = dumps(file_contents, indent=4)
                        file.writelines(json_object)

                case self._file_mode_append:
                    if file_type == self._file_type_text:
                        file.writelines(file_contents)

                    if file_type == self._file_type_json:
                        json_object = dumps(file_contents, indent=4)
                        file.writelines(json_object)

                case _:
                    return None

        except FileNotFoundError as err:
            self._log_handler.create_log(
                log_type="error",
                log_message=f"File not found. Possible missing directory. {err}")

            return None

        except JSONDecodeError as err:
            self._log_handler.create_log(
                log_type="error",
                log_message=f"Error reading json file object. {err}")

            return None

    def adapter_creates_file(
            self,
            file_type: str,
            file_path: str, file_mode: str,
            file_contents: (str | dict[str, str])) -> (str | dict[str, str] | None):
        """Adapter method to create file based on the provided file type.
        
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

        # File creation.
        with open(file=file_path, mode=file_mode, encoding="UTF-8") as file:
            return self._file_operator(file_type=file_type,
                                       file_mode=file_mode, file=file, file_contents=file_contents)