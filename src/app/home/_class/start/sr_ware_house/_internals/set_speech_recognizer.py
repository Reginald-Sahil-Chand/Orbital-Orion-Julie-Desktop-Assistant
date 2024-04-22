"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

set_speech_recognizer.py:
=========================
This file contains a class that creates a speech recognizer using the create_speech_recognizer -
method.

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

# Include external packages and modules.
from speech_recognition import Recognizer, Microphone, AudioData # type: ignore

# Include custom packages and modules.
from src.app.design_pattern.strategy.abstract.blueprint.abstract_set_speech_recognizer\
    .abstract_set_speech_recognizer import AbstractSetSpeechRecognizer
from src.app.utility.handler._class.text_to_speech.text_to_speech\
    import TextToSpeech


@dataclass
class SetSpeechRecognizer(AbstractSetSpeechRecognizer):
    """Class responsible to create speech recognizer based on the chosen speech_recognizer."""

    # Instantiate TextToSpeechHandler.
    _text_to_speech_handler: TextToSpeech = field(default_factory=TextToSpeech)

    # Instantiate Recognizer and Microphone.
    _recognizer: Recognizer = Recognizer()
    _microphone: Microphone = Microphone()

    _voice_query: str = ""

    def initiate_speech_recognition(self, speech_recognizer: str) -> str:
        """This method initiates the create_speech_recognizer method.

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

        self._text_to_speech_handler.create_text_to_speech(
            text_to_produce_speech="How can I assist you today?")

        with self._microphone as source:
            audio: AudioData = self._recognizer.listen(source) # type: ignore

        self._voice_query = self.create_speech_recognizer(
            speech_recognizer=speech_recognizer,
            recognizer=self._recognizer,
            audio=audio,
            text_to_speech_handler=self._text_to_speech_handler,
            should_announce_error_message=True)

        if self._voice_query.strip():
            self._text_to_speech_handler.create_text_to_speech(
            text_to_produce_speech="Please wait!")

        return self._voice_query.lower()

    def initiate_speech_recognition_once(self, speech_recognizer: str) -> str:
        """This method initiates the create_speech_recognizer method.

        Summary:
            - After the initiation of the create_speech_recognizer method the,
            returned value (voice input) from that method is passed down to the required,
            classes and functions that use it as needed.

        Args:
            - speech_recognizer (str): The speech recognizer name that will be used,
            to distinguish between the supported speech recognizer's.
        
        Returns: 
            - str: The voice query.

        Note: Only use this method if your are to initiate voice recognition once,
        """

        with self._microphone as source:
            audio: AudioData = self._recognizer.listen(source) # type: ignore

        self._voice_query = self.create_speech_recognizer(
            speech_recognizer=speech_recognizer,
            recognizer=self._recognizer,
            audio=audio,
            text_to_speech_handler=self._text_to_speech_handler)

        return self._voice_query.lower()
