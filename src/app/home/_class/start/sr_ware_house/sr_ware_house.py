"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

sr_ware_house.py:
=================
This file contains a class to get voice inputs and perform tasks based on the given voice input.
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

# Include internal typings.
from typing import Dict

# Include external packages and modules.
from speech_recognition import Recognizer, Microphone # type: ignore
from memory_profiler import profile # type: ignore

# Include custom packages and modules.
from src.app.utility.handler._class.text_to_speech.text_to_speech\
    import TextToSpeech
from src.app.home._class.start.sr_ware_house._internals.set_speech_recognizer\
    import SetSpeechRecognizer
from src.app.home._class.start.sr_ware_house._internals.initiate_julie import initiate_julie
from src.app.utility.data._module.wake_words import wake_words_to_activate_julie

# * GLOBAL VARIABLES ! (USE WITH CARE)
# Define announcement messages.
_ANNOUNCEMENT_MESSAGE: Dict[str, str] = {
    "online_message": "Julie is online. Say \"Hey Julie\"\n",
    "adjusting_noise": "Adjusting for ambient noise. Please wait.\n",
    "termination_message": """The program has been terminated using the Control + C shortcut.
Thank you for using my service.\nWishing you a great day ahead!\n"""
    }

# ! DANGER: DISABLE ALL @profile DECORATOR'S BEFORE PUSHING THE CODE INTO PRODUCTION.
# ! THIS IS TO AVOID UNNECESSARY MEMORY CONSUMPTION.


@dataclass
class SRWareHouse():
    """Class to get voice inputs, and perform tasks based on the given input."""

    # Instantiate TextToSpeechHandler.
    _text_to_speech_handler: TextToSpeech = field(default_factory=TextToSpeech)

    # Instantiate SetSpeechRecognizer.
    _set_speech_recognizer: SetSpeechRecognizer = field(default_factory=SetSpeechRecognizer)

    # Instantiate Recognizer and Microphone.
    _recognizer: Recognizer = Recognizer()
    _microphone: Microphone = Microphone()

    @profile
    def initiate_speech_recognition (self, speech_recognizer: str) -> None:
        """Method that initiates the speech recognition process.

        Args:
            - speech_recognizer (str): The speech recognizer name that will be used,
            to distinguish between the supported speech recognizer's.
        
        Returns:
            - None.
        """

        try:
            self._text_to_speech_handler.create_text_to_speech(
                text_to_produce_speech=_ANNOUNCEMENT_MESSAGE["adjusting_noise"])

            with self._microphone as source:
                self._recognizer.adjust_for_ambient_noise(source) # type: ignore

            print(_ANNOUNCEMENT_MESSAGE["online_message"])
            self._text_to_speech_handler.create_text_to_speech(
                text_to_produce_speech=_ANNOUNCEMENT_MESSAGE["online_message"])

            while True:
                query = self._set_speech_recognizer.initiate_speech_recognition_once(
                speech_recognizer=speech_recognizer)

                if query in wake_words_to_activate_julie:
                    initiate_julie(
                        speech_recognizer=speech_recognizer,
                        set_speech_recognizer=self._set_speech_recognizer,
                        text_to_speech_handler=self._text_to_speech_handler)

        except KeyboardInterrupt:
            print(_ANNOUNCEMENT_MESSAGE["termination_message"])
            self._text_to_speech_handler.create_text_to_speech(
                text_to_produce_speech=_ANNOUNCEMENT_MESSAGE["termination_message"])
