"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

text_to_speech_handler.py:
==========================
Class to convert a given text into speech.

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

# * NOTE: "# type: ignore" has been used at some places because, some packages,
# * Does not have a specific stub file hence pylint / pylance are unable to infer types.
# * Thus to avoid unnecessary errors and warnings, making the code base noisy, I decided to,
# * Ignore types for some parts of the code.

# Include built-in packages and modules.
from dataclasses import dataclass, field

# Include internal typings.
from typing import Any

# Include external packages and modules.
import pyttsx3 # type: ignore

# Include custom packages and modules.
from src.app.utility.handler.log_handler.log_handler import LogHandler # type: ignore


@dataclass
class TextToSpeechHandler:
    """Class to convert a given text into speech."""

    # Instantiate pyttsx3.
    _engine: pyttsx3.Engine = pyttsx3.init() # type: ignore

    # Instantiate LogHandler.
    _log_handler: LogHandler = field(default_factory=LogHandler)

    def create_text_to_speech_announcer(self, text_to_produce_speech: str) -> None:
        """Method to convert a given text into speech based on the text_to_produce_speech string.
        
        Args:
            - text_to_produce_speech (str) - The text that needs to be converted into speech.

        Returns: None.
        """

        try:
            if not text_to_produce_speech.strip():
                raise ValueError("Error: text_to_produce_speech parameter cannot be empty.")

            # Set speaker (speaking) rate.
            # Speed at which the speaker will read the text.
            self._engine.setProperty('rate', 175) # type: ignore

            # Get supported voices. (Device Specific.)
            # * ON WINDOWS: [0] = MALE VOICE, [1] = FEMALE VOICE, BOTH (DEFAULTS).
            voices: Any = self._engine.getProperty('voices') # type: ignore
            self._engine.setProperty('voice', voices[1].id) # type: ignore

            # Speak text.
            self._engine.say(text=text_to_produce_speech) # type: ignore
            self._engine.runAndWait() # type: ignore

        except ValueError as err:
            self._log_handler.create_log(
                log_type="error",
                log_message=f"Error converting text to speech: {err}")

        except Exception as err:
            error_message = f"Unexpected error occurred: {err}"
            self._log_handler.create_log(log_type="error", log_message=error_message)

            # Reraise the exception for higher-level handling.
            raise
