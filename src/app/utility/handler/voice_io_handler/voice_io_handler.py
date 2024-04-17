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

# Include external packages and modules.
from speech_recognition import Recognizer, Microphone # type: ignore

# Include custom packages and modules.
from src.app.utility.handler.text_to_speech_handler.text_to_speech_handler\
    import TextToSpeechHandler
from src.app.design_pattern.strategy.abstract.blueprint.abstract_voice_io_handler\
    .abstract_voice_io_handler import AbstractVoiceIoHandler


@dataclass
class VoiceIoHandler(AbstractVoiceIoHandler):
    """Class to get voice inputs, and perform tasks based on the given input."""

    # Instantiate TextToSpeechHandler.
    _text_to_speech_handler: TextToSpeechHandler = field(default_factory=TextToSpeechHandler)

    # Instantiate Recognizer and Microphone.
    _recognizer: Recognizer = Recognizer()
    _microphone: Microphone = Microphone()

    # Stores the user's current speech at runtime.
    _voice_input_value: (str | None) = ""

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

        # Define announcement messages.
        noise_adjustment_message: str = (
            "A moment of silence please. Doing adjustments for ambient noise.")

        how_may_i_help_you_message: str = "How may I help you?\n"
        recognizing_voice_input_message: str = "Got it! Please wait. Recognizing voice input."
        voice_input_recognized_message: str = "You said"

        could_not_recognize_voice_input_message: str = (
            "Oops! I apologize because, I couldn't understand what you said. "
            "Could you please try again?\n")

        try:
            if speech_recognizer not in self._supported_speech_recognizer:
                raise TypeError(
                    f"Alert: The type {speech_recognizer} is not supported.\n"
                    f"Supported types are {self._supported_speech_recognizer_types}")

            print(noise_adjustment_message)
            self._text_to_speech_handler.create_text_to_speech_announcer(
                text_to_produce_speech=noise_adjustment_message)

            with self._microphone as source:
                self._recognizer.adjust_for_ambient_noise(source) # type: ignore

            while True:
                print(how_may_i_help_you_message)
                self._text_to_speech_handler.create_text_to_speech_announcer(
                    text_to_produce_speech=how_may_i_help_you_message)

                with self._microphone as source:
                    audio = self._recognizer.listen(source) # type: ignore

                print(recognizing_voice_input_message)
                self._text_to_speech_handler.create_text_to_speech_announcer(
                    text_to_produce_speech=recognizing_voice_input_message)

                self._voice_input_value = self.create_voice_recognizer(
                    speech_recognizer=speech_recognizer,
                    recognizer=self._recognizer,
                    audio=audio,
                    text_to_speech_handler=self._text_to_speech_handler,
                    voice_input_recognized_message=voice_input_recognized_message,
                    could_not_recognize_voice_input_message=could_not_recognize_voice_input_message)

                # Print returned value.
                if isinstance(self._voice_input_value, str):
                    print(self._voice_input_value.lower())

        except KeyboardInterrupt:
            print("Dear user, you have entered \"ctrl+c\", hence the program has been terminated.")
            self._text_to_speech_handler.create_text_to_speech_announcer(
                text_to_produce_speech=(
                    "Dear user, you have terminated the program by pressing the "
                    "control key with the letter C key available on your keyboard. "
                    "Good Bye and Take Care"))
