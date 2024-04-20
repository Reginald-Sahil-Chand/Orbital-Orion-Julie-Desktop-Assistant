"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

abstract_set_speech_recognizer.py:
==================================
Acts as a blueprint for the SetSpeechRecognizer class.
sr equals Speech Recognition.

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
from typing import Dict, Any, Callable, List

# Include custom packages and modules.
from src.app.utility.helper._module.speech_recognizer.google import google_speech_recognizer


@dataclass
class AbstractSetSpeechRecognizer(ABC):
    """Abstract class to handle speech recognizer's."""

    _supported_speech_recognizer: Dict[str, Callable[..., (str | Any)]] =  field(
        default_factory=lambda: {
        "google_speech_recognizer": google_speech_recognizer.google_speech_recognizer,
    })

    def __post_init__(self):
        self._supported_speech_recognizer_types: List[str] = (
            list(k for k in self._supported_speech_recognizer))

    should_announce_error_message: bool = False

    @abstractmethod
    def initiate_speech_recognition(self, speech_recognizer: str) -> str:
        """Abstract method that initiates the create_speech_recognizer method.

        Summary:
            - After the initiation of the create_speech_recognizer method the,
            returned value (voice input) from that method is passed down to the required,
            classes and functions that use it as needed.

        Args:
            - speech_recognizer (str): The speech recognizer name that will be used,
            to distinguish between the supported speech recognizer's.
        
        Returns: 
            - str: The voice query.
        """

    def create_speech_recognizer(
            self,
            speech_recognizer: str,
            recognizer: Any,
            audio: Any,
            text_to_speech_handler: Any) -> (str | None):
        """Creates a voice recognizer based on the specified speech recognizer name.

        Args:
            - self: The instance of the class.
            - speech_recognizer (str): The name of the speech recognizer to create.
            - recognizer (Any): The recognizer object used for speech recognition.
            - audio (Any): The audio input to be recognized.
            - text_to_speech_handler (Any): The handler for converting text to speech.

        Returns:
            - str | None: The recognized voice input as a string, or None if recognition fails.

        Note:
            - This method checks if the specified speech recognizer is supported.
            - If supported, it calls the corresponding function from
            _supported_speech_recognizer to create the voice recognizer and perform
            speech recognition.
        """

        if speech_recognizer not in self._supported_speech_recognizer:
            raise TypeError(
                f"Alert: The type {speech_recognizer} is not supported.\n"
                f"Supported types are {self._supported_speech_recognizer_types}")

        if speech_recognizer in self._supported_speech_recognizer:
            func_speech_recognizer = self._supported_speech_recognizer[speech_recognizer]
            query: str = func_speech_recognizer(
                recognizer=recognizer,
                audio=audio,
                text_to_speech_handler=text_to_speech_handler,
                should_announce_error_message=self.should_announce_error_message)

            return query

        return None
