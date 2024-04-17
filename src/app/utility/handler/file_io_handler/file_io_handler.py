"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

file_io_handler.py:
===================
This file contains FileIoHandler class, responsible to handle file operations.

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
from os import path

# Include internal typings.
from typing import Any, Dict, Tuple

# Include custom packages and modules.
from src.app.design_pattern.adapter.abstract.blueprint.abstract_file_io_handler\
    .abstract_file_io_handler import AbstractFileIoHandler
from src.app.utility.handler.log_handler.log_handler import LogHandler
from src.app.utility.handler.directory_io_handler.directory_io_handler import DirectoryIoHandler
from src.app.utility.helper.validation.custom_value_and_type_validation\
    .custom_value_and_type_validation import validate_if_value_is_empty,\
        validate_if_type_does_not_match, validate_file_contents


# Define custom csv file exception.
# I haven't moved this exception to its separate folder because this,
# exception only handles csv locally.
class FileTypeWillBeSupportedSoonError(Exception):
    """Class to handle CSV File unsupported error."""

@dataclass
class FileIoHandler(AbstractFileIoHandler):
    """Class to handle create_file_operation instantiation."""

    # Instantiate LogHandler.
    log_handler: LogHandler = field(default_factory=LogHandler)

    # Instantiate DirectoryHandler.
    directory_io_handler: DirectoryIoHandler = field(default_factory=DirectoryIoHandler)

    # Stores file contents.
    returned_file_contents: (str | Dict[Any, Any] | None) = field(default_factory=lambda: {})

    def create_file_operation(self,
                              file_contents: (str | dict[str, str]),
                              **kwargs: str) -> (str | dict[str, str] | None):
        """This method is responsible for creating the file operations.

        File operations in this context are as follows:
            - File Operation [1]: Read file.
            - File Operation [2]: Write file.
            - File Operation [3]: Append file.

        Args:
            - self (Self@AbstractFileIoHandler): Refers to the base class.
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

        # Define file data for file type and file mode checking.
        _file_data: Dict[str, dict[str, str]] = {
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

        # Define default values for the used keyword arguments.
        directory_name_or_name_with_path: str = kwargs.get("directory_path", "")
        file_type: str = kwargs.get("file_type", "")
        file_name: str = kwargs.get("file_name", "")
        file_mode: str = kwargs.get("file_mode", "")

        # Error handling.
        _file_types: Tuple[str, ...] = tuple(key for key in _file_data["file_types"])
        _file_modes: Tuple[str, ...] = tuple(key for key in _file_data["file_modes"].values())
        _min_file_contents_length = 1

        if file_type == _file_data["file_types"]["csv"]:
            raise FileTypeWillBeSupportedSoonError(
                "CSV File type will be supported soon. Sorry for the inconvenience caused.")

        # Invoke custom value and type validation functions.
        # * Refer to utility/helpers/validation folder(s) to learn more.
        validate_if_value_is_empty(
            value=directory_name_or_name_with_path,
            value_name_to_be_validated_on="directory")
        validate_if_type_does_not_match(given_type=file_type, supported_types=_file_types)
        validate_if_value_is_empty(
            value=file_name,
            value_name_to_be_validated_on="file name")
        validate_if_type_does_not_match(given_type=file_mode, supported_types=_file_modes)
        validate_file_contents(file_contents=file_contents,
                               min_file_contents_length=_min_file_contents_length)

        _file_name_with_path: str = path.join(directory_name_or_name_with_path, file_name)

        try:
            self.directory_io_handler.create_directory(
                directory_path=directory_name_or_name_with_path)

            self.returned_file_contents = self.adapter_creates_file(
                file_type=file_type, file_name=_file_name_with_path,
                                      file_mode=file_mode, file_contents=file_contents)

        except FileNotFoundError as err:
            self._log_handler.create_log(
                log_type="error",
                log_message=f"File not found. Possible missing directory. {err}")

        return self.returned_file_contents
