"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

abstract_file_operation.py:
===========================
Acts as a blueprint for the file_operation utility class.

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
from abc import ABC, abstractmethod

# Include internal typings.
from typing import IO, Any

# Include external packages and modules.
from json import JSONDecodeError, load, dumps

# Include custom packages and modules.
from src.app.utility.handler._class.log_handler.log_handler import LogHandler


@dataclass
class AbstractFileOperation(ABC):
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
                              file_contents: (str | dict[str, str]),
                              **kwargs: str) -> (str | dict[str, str] | None):
        """This method is responsible for creating the file operations.

        File operations in this context are as follows:
            - File Operation [1]: Read file.
            - File Operation [2]: Write file.
            - File Operation [3]: Append file.

        Args:
            - self: Creates instance of the class.
            - file_contents (str): File contents refer to the content of the file.
                    - Here content means when you are creating a file, reading or writing a file,
                    what does the file contain, this can be a list of items, block of text or,
                    basically anything, just like notes.

        Kwargs:
            - directory_name_or_name_with_path (str): Directory path refers to the path
            where the file will be created or read from that includes the creation of the
            directory if it doesn't exists.

            - file_type (str): There are three currently supported file types:
                - File Type [1]: text.
                - File Type [1]: json.
                - File Type [1]: csv. (Support to be added at a later date.)

            - file_name (str): File name refers to the file name. Example file.txt

            - file_mode (str): File mode refers to the mode for the file operation.
                - There are three file modes currently supported:
                    - File Mode [1]: "r" => read file.
                    - File Mode [2]: "w" => write file.
                    - File Mode [3]: "a" => append to current existing file.

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
            - self: Creates instance of the class.
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
                    if file_type in self._file_type_text or file_type in self._file_mode_append:
                        file.writelines(file_contents)

                    if file_type in self._file_type_json or file_type in self._file_type_json:
                        json_object = dumps(file_contents, indent=4)
                        file.writelines(json_object)

                case _:
                    return None

        except FileNotFoundError as err:
            self._log_handler.create_log(
                log_type="error",
                log_message=f"File not found. Possible missing directory. {err}")

        except JSONDecodeError as err:
            self._log_handler.create_log(
                log_type="error",
                log_message=f"Error reading json file object. {err}")

        except ValueError as err:
            self._log_handler.create_log(
                log_type="error",
                log_message=f"{file_mode or file_type} cannot be empty. {err}")

        return None

    def adapter_creates_file(
            self,
            file_type: str,
            file_name: str, file_mode: str,
            file_contents: (str | dict[str, str])) -> (str | dict[str, str] | None):
        """Adapter method to create file based on the provided file type.
        
        Args:
            - self: Creates instance of the class.
            - file_type (str): There are three currently supported file types:
                - File Type [1]: text.
                - File Type [1]: json.
                - File Type [1]: csv. (Support to be added at a later date.)

            - file_name (str): File name refers to the file name. Example file.txt

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
        with open(file=file_name, mode=file_mode, encoding="UTF-8") as file:
            return self._file_operator(file_type=file_type,
                                       file_mode=file_mode,
                                       file=file,
                                       file_contents=file_contents)
