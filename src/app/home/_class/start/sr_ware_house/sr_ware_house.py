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
from time import sleep

# Include internal typings.
from typing import Dict

# Include external packages and modules.
from speech_recognition import Recognizer, Microphone # type: ignore
from memory_profiler import profile # type: ignore
import schedule

# Include custom packages and modules.
from src.app.design_pattern.strategy.abstract.blueprint\
    .abstract_sr_ware_house.abstract_sr_ware_house import AbstractSpeechRecognitionWareHouse
from src.app.utility.handler._class.text_to_speech.text_to_speech\
    import TextToSpeech
from src.app.utility.handler._class.artificial_intelligence\
    .googles_gemini_ai.gemini_ai import GeminiAi
from src.app.utility.helper._module.app_opener.app_opener import open_application
from src.app.utility.data._module.wake_words import wake_words_to_open_apps,\
    wake_words_to_activate_julie, wake_words_to_self_describe

# * GLOBAL VARIABLES ! (USE WITH CARE)
# Define announcement messages.
_ANNOUNCEMENT_MESSAGE: Dict[str, str] = {
    "online_message": "Julie is online. Say \"Hey Julie\"\n",
    "adjusting_noise": "Adjusting for ambient noise. Please wait.\n",
    "help_request": "How can I assist you today?\n",
    "processing_voice_input": "Searching for relevant results. Please wait!\n",
    "termination_message": """The program has been terminated using the Control + C shortcut.
Thank you for using my service.\nWishing you a great day ahead!\n"""
    }

# ! DANGER: DISABLE ALL @profile DECORATOR'S BEFORE PUSHING THE CODE INTO PRODUCTION.
# ! THIS IS TO AVOID UNNECESSARY MEMORY CONSUMPTION.


@dataclass
class SRWareHouse(AbstractSpeechRecognitionWareHouse):
    """Class to get voice inputs, and perform tasks based on the given input."""

    # Instantiate TextToSpeechHandler.
    _text_to_speech_handler: TextToSpeech = field(default_factory=TextToSpeech)

    # Instantiate GeminiHandler.
    _gemini_handler: GeminiAi = field(default_factory=GeminiAi)

    # Instantiate Recognizer and Microphone.
    _recognizer: Recognizer = Recognizer()
    _microphone: Microphone = Microphone()

    _voice_query: str = ""
    _query: str = ""

    @profile
    def initiate_speech_recognition (self, speech_recognizer: str) -> None:
        """Method that initiates the create_voice_recognizer method.

        Summary:
            - After the initiation of the create_voice_recognizer method the,
            returned value (voice input) from that method is passed down to the required,
            classes and functions that use it as needed.

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

            schedule.every(1).second.do(job_func=self._initiate_julie( # type: ignore
                speech_recognizer=speech_recognizer))

            while True:
                schedule.run_pending()
                sleep(1)

        except KeyboardInterrupt:
            print(_ANNOUNCEMENT_MESSAGE["termination_message"])
            self._text_to_speech_handler.create_text_to_speech(
                text_to_produce_speech=_ANNOUNCEMENT_MESSAGE["termination_message"])

    @profile
    def _set_speech_recognizer(self, speech_recognizer: str) -> None:
        """Initiates voice recognition process.

        Args:
            - speech_recognizer (str): The type of speech recognizer to use.

        Returns: 
            - None.
        """

        if speech_recognizer not in self._supported_speech_recognizer:
            raise TypeError(
                f"Alert: The type {speech_recognizer} is not supported.\n"
                f"Supported types are {self._supported_speech_recognizer_types}")

        self._text_to_speech_handler.create_text_to_speech(
            text_to_produce_speech=_ANNOUNCEMENT_MESSAGE["help_request"])

        with self._microphone as source:
            audio = self._recognizer.listen(source) # type: ignore

        self._text_to_speech_handler.create_text_to_speech(
            text_to_produce_speech=_ANNOUNCEMENT_MESSAGE["processing_voice_input"])

        self._voice_query = str(self.create_speech_recognizer(
        speech_recognizer=speech_recognizer,
        recognizer=self._recognizer,
        audio=audio,
        text_to_speech_handler=self._text_to_speech_handler))

        self._query = self._voice_query.lower()
        wake_words_to_open_apps["wake_with_open"] = f"open {self._query[5::]}"
        wake_words_to_open_apps["wake_with_go_to"] = f"open {self._query[6::]}"

    @profile
    def _initiate_julie(self, speech_recognizer: str) -> None:
        """Initiates awakening of Julie.

        Args:
            - speech_recognizer (str): The type of speech recognizer to use.

        Returns: 
            - None.
        """

        while True:
            with self._microphone as source:
                audio = self._recognizer.listen(source) # type: ignore

            self._voice_query = str(self.create_speech_recognizer(
                speech_recognizer=speech_recognizer,
                recognizer=self._recognizer,
                audio=audio,
                text_to_speech_handler=self._text_to_speech_handler))

            if self._voice_query.lower() in wake_words_to_activate_julie:
                self.should_announce_error_message = True

                while True:
                    self._set_speech_recognizer(speech_recognizer=speech_recognizer)
                    if ((self._query == wake_words_to_open_apps["wake_with_open"])
                        or
                        (self._query == wake_words_to_open_apps["wake_with_go_to"])):
                        open_application(query=(
                            wake_words_to_open_apps["wake_with_open"]
                            or wake_words_to_open_apps["wake_with_go_to"]),
                            text_to_speech_handler=self._text_to_speech_handler)

                    elif self._query in wake_words_to_self_describe:
                        # TODO: Update the message below, and handle the message
                        # TODO: in a separate variable.
                        self._text_to_speech_handler.create_text_to_speech(
                            text_to_produce_speech=(
                                "I'm Julie, a desktop assistant created by Reginald Chand"
                                "He created me as a personal project."))

                    else:
                        if self._query.strip():
                            self._text_to_speech_handler.create_text_to_speech(
                            text_to_produce_speech=(
                                "I'm sorry! I cant help you with this."))

            else:
                # * USE ARTIFICIAL INTELLIGENCE (GOOGLE'S GEMINI).
                user_requested_prompt: str = (
                    self._gemini_handler.initiate_gemini_ai(prompt=str(self._voice_query)))

                remove_asterisk_from_prompt = user_requested_prompt.replace("*", "")

                self._text_to_speech_handler.create_text_to_speech(
                    text_to_produce_speech=remove_asterisk_from_prompt)
