"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

user_information.py:
====================
Class to get the user information and render it on the console.

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
import re
from json import JSONDecodeError, loads
from os.path import exists

# Include internal typings.
from typing import Dict, List

# Include custom packages and modules.
from src.app.utility.handler._class.input_handler.input_handler import InputHandler
from src.app.utility.handler._class.file_operation.file_operation import FileOperation
from src.app.utility.handler._class.log_handler.log_handler import LogHandler
from src.app.utility.handler._class.text_to_speech.text_to_speech\
    import TextToSpeech


@dataclass
class UserInformation:
    """Class to get the user information and render it on the console.
    
    Example:
        - Ask user for the username:
        - username = "Reginald Chand"
        - Display name on the console = Welcome Reginald Chand
    """

    # Instantiate InputHandler.
    _handle_user_input: InputHandler = field(default_factory=InputHandler)

    # Instantiate FileIoHandler.
    _file_operation: FileOperation =  field(default_factory=FileOperation)

    # Instantiate LogHandler.
    _log_handler: LogHandler =  field(default_factory=LogHandler)

    # Instantiate TextToSpeech.
    _text_to_speech: TextToSpeech =  field(default_factory=TextToSpeech)

    # The user configuration data, default file path.
    _file_path: str = "oojda/data/configs/user/user_info.json"

    _user_data: Dict[str, str] = field(default_factory=lambda: {})

    def _set_user_name(self) -> str:
        """Method to ask the user to enter username.

        Returns:
            - ask_user_for_username (str): The name of the user.
        """

        user_name: str = ""
        _minimum_length_for_username: int = 4

        _symbol_pattern: re.Pattern[str] = re.compile(r'[^\w\s]')
        _digit_pattern: re.Pattern[str] = re.compile(r'\d')

        while True:
            user_name: str = str(self._handle_user_input.create_input(
            input_type="str",
            input_display_message="\nDear user, please enter your name >> "))

            # Handle errors.
            if not user_name.strip():
                print("\nWarning: USERNAME CANNOT BE EMPTY")

            elif re.search(_digit_pattern, user_name):
                print("Warning: USERNAME CANNOT BE A DIGIT")

            elif re.search(_symbol_pattern, user_name):
                print("Warning: SYMBOLS ARE NOT ALLOWED IN USERNAME")

            elif len(user_name) < _minimum_length_for_username:
                print(
                    f"Warning: USERNAME CANNOT BE LESS THAN "
                    f"{_minimum_length_for_username} CHARACTERS")

            else:
                # If input errors equal 0.
                return user_name

    def create_user_information(self) -> None:
        """Method to save the username to the required config file and display it on console."""

        if not exists(self._file_path):
            user_name: str = self._set_user_name()

            # Define required user data.
            self._user_data: Dict[str, str] = {
                "WARNING":
                "FILE GENERATED BY ORBITAL ORION JULIE DESKTOP ASSISTANT [DO NOT DELETE]",
                "InitialProgramRun": "True",
                "Username": user_name
            }

            self._file_operation.create_file_operation(
                    file_contents=self._user_data,
                    directory_path="oojda/data/configs/user",
                    file_type="json",
                    file_name="user_info.json",
                    file_mode="w")

            self._log_handler.create_log(
                log_type="info",
                log_message=f"User {user_name} has been successfully created.")

            print(f"\nWelcome {user_name}\n")

            user_name_words: List[str] = user_name.split()

            welcome_text:str = f"""Hello {user_name_words[0]}.
            Welcome to Orbital Orion's Julie Desktop Assistant.
            I'm Julie, your personal desktop assistant.
            I was created by Reginald Sahil Chand as a personal project.\n
            """

            self._text_to_speech.create_text_to_speech(
                text_to_produce_speech=welcome_text)

        else:
            try:
                created_user_info = self._file_operation.create_file_operation(
                        file_contents="Read File",
                        directory_path="oojda/data/configs/user",
                        file_type="json",
                        file_name="user_info.json",
                        file_mode="r")

                # Load json file as a python dictionary.
                user_data: Dict[str, str] = loads(str(created_user_info).replace("'", "\""))

                # Get the user name.
                user_name: str =  user_data["Username"]
                user_name_words: List[str] = user_name.split()

                print(f"Welcome {user_name}\n")

                self._text_to_speech.create_text_to_speech(
                    text_to_produce_speech=f"Hello {user_name_words[0]}.")

            except JSONDecodeError:
                print("Error: user_info.json file is empty.\n"
                      "Please try deleting \"user_info.json\" file from oojda folder.\n"
                      "And re-run this software to fix this error.")
