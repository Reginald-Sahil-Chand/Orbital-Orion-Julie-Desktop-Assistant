"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

voice_io_handler.py:
====================
This file contains a class to get voice inputs and perform tasks based on the given voice input.

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
from typing import Dict, Tuple

# Include external packages and modules.
from speech_recognition import Recognizer, Microphone # type: ignore

# Include custom packages and modules.
from src.app.utility.handler.text_to_speech_handler.text_to_speech_handler\
    import TextToSpeechHandler
from src.app.design_pattern.strategy.abstract.blueprint.abstract_voice_io_handler\
    .abstract_voice_io_handler import AbstractVoiceIoHandler
from src.app.utility.handler.artificial_intelligence_handler\
    .gemini_handler.gemini_handler import GeminiHandler


@dataclass
class VoiceIoHandler(AbstractVoiceIoHandler):
    """Class to get voice inputs, and perform tasks based on the given input."""

    # Instantiate TextToSpeechHandler.
    _text_to_speech_handler: TextToSpeechHandler = field(default_factory=TextToSpeechHandler)

    # Instantiate GeminiHandler.
    _gemini_handler: GeminiHandler = field(default_factory=GeminiHandler)

    # Instantiate Recognizer and Microphone.
    _recognizer: Recognizer = Recognizer()
    _microphone: Microphone = Microphone()

    # Define announcement messages.
    announcement_message: Dict[str, str] = field(default_factory=lambda: {
        "noise_adjustment_message": (
            "A moment of silence please. Doing adjustments for ambient noise."),
        "how_may_i_help_you_message": "How may I help you?\n",
        "recognizing_voice_input_message": "Got it! Please wait. Recognizing voice input.",
        "voice_input_recognized_message": "You said",
        "could_not_recognize_voice_input_message": (
            "Oops! I apologize because, I couldn't understand what you said. "
            "Could you please try again?\n")
    })

    # Stores the user's current speech at runtime.
    _voice_input_value: (str | None) = ""

    def _set_speech_recognizer(self, speech_recognizer: str) -> None:
        """Initiates voice recognition process.

        Args:
            - speech_recognizer (str): The type of speech recognizer to use.

        Returns: None
        """

        print(self.announcement_message["how_may_i_help_you_message"])
        self._text_to_speech_handler.create_text_to_speech_announcer(
            text_to_produce_speech=self.announcement_message["how_may_i_help_you_message"])

        with self._microphone as source:
            audio = self._recognizer.listen(source) # type: ignore

        print(self.announcement_message["recognizing_voice_input_message"])
        self._text_to_speech_handler.create_text_to_speech_announcer(
            text_to_produce_speech=self.announcement_message["recognizing_voice_input_message"])

        self._voice_input_value = self.create_voice_recognizer(
            speech_recognizer=speech_recognizer,
            recognizer=self._recognizer,
            audio=audio,
            text_to_speech_handler=self._text_to_speech_handler,
            voice_input_recognized_message=(
                self.announcement_message["voice_input_recognized_message"]),
            could_not_recognize_voice_input_message=(
                self.announcement_message["could_not_recognize_voice_input_message"]))

    def get_voice_input(self, speech_recognizer: str) -> None:
        """Method that initiates the create_voice_recognizer method.

        Summary:
            - After the initiation of the create_voice_recognizer method the,
            returned value (voice input) from that method is passed down to the required,
            classes and functions that use it as needed.

        Args:
            - speech_recognizer (str): The speech recognizer name that will be used,
            to distinguish between the supported speech recognizer's.
        
        Returns: None
        """

        # Define AI wake words.
        ai_wake_words: Tuple[str, ...] = ("use ai", "use gemini", "use artificial intelligence")

        try:
            if speech_recognizer not in self._supported_speech_recognizer:
                raise TypeError(
                    f"Alert: The type {speech_recognizer} is not supported.\n"
                    f"Supported types are {self._supported_speech_recognizer_types}")

            print(self.announcement_message["noise_adjustment_message"])
            self._text_to_speech_handler.create_text_to_speech_announcer(
                text_to_produce_speech=self.announcement_message["noise_adjustment_message"])

            with self._microphone as source:
                self._recognizer.adjust_for_ambient_noise(source) # type: ignore

            while True:
                self._set_speech_recognizer(speech_recognizer=speech_recognizer)

                if isinstance(self._voice_input_value, str):
                    if self._voice_input_value.lower() in ai_wake_words:
                        print("USING AI \"GEMINI PRO.\"\n")
                        self._text_to_speech_handler.create_text_to_speech_announcer(
                            text_to_produce_speech="Using AI, Gemini Pro.")

                        self._set_speech_recognizer(speech_recognizer=speech_recognizer)

                        print("Generating Content. Please Wait. It might take some time.\n")
                        self._text_to_speech_handler.create_text_to_speech_announcer(
                            text_to_produce_speech=(
                                "Generating Content. Please Wait. It might take some time."))

                        user_requested_prompt: str = self._gemini_handler.initiate_gemini_ai(
                            prompt=str(self._voice_input_value))

                        print(f"{user_requested_prompt}\n")
                        remove_asterisk_from_prompt = user_requested_prompt.replace("*", "")

                        self._text_to_speech_handler.create_text_to_speech_announcer(
                            text_to_produce_speech=remove_asterisk_from_prompt)

        except KeyboardInterrupt:
            print("Dear user, you have entered \"ctrl+c\", hence the program has been terminated.")
            self._text_to_speech_handler.create_text_to_speech_announcer(
                text_to_produce_speech=(
                    "Dear user, you have terminated the program by pressing the "
                    "control key with the letter C key available on your keyboard. "
                    "Good Bye and Take Care"))
