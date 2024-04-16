"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

voice_io_handler.py:
====================
This file contains a class to get voice inputs.

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
from random import choice

# Include internal types.
from typing import Any

# Include external packages and modules.
from speech_recognition import ( # type: ignore
    Recognizer,
    Microphone,
    UnknownValueError,
    RequestError,
)

# Include custom packages and modules.
from src.app.utility.handler.text_to_speech_handler.text_to_speech_handler\
    import TextToSpeechHandler

@dataclass
class VoiceIoHandler:
    """Class to get voice inputs."""

    # Instantiate TextToSpeechHandler.
    _text_to_speech_handler: TextToSpeechHandler = field(default_factory=TextToSpeechHandler)

    # Instantiate Recognizer and Microphone.
    _recognizer: Recognizer = Recognizer()
    _microphone: Microphone = Microphone()

    # Stores the voice input.
    _voice_input: str = ""

    def get_voice_input(self) -> (str | None):
        """Method that takes voice inputs and returns the input as a string.
        
        Returns (str): The voice_input, or None.
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
        request_error_message_for_google_speech_recognition: str = (
            "Uh oh! Couldn't request results from Google Speech Recognition service.\n"
            "Make sure you are connected to the internet. Good Bye.\n")

        # Define wake words.
        # * You can use these words to implement functionalities to only respond
        # * If voice_input_value matches any of these words.
        wake_words: list[str] = [
            "hi", "hey", "hello", "Julie",
            "hi Julie", "hello Julie", "hey Julie"
        ]

        greetings: list[str] = [
            "Hi!", "Hello!", "Hey!", "Ola!",
            "Bula",
        ]

        random_greeting: str = choice(greetings)

        try:
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

                # TODO: If you are using more than 1 speech recognition engine then,
                # TODO: Please create each engine as a separate method or class, and invoke here.
                # TODO: If you are to implement a class, consider creating it in a separate file.
                # TODO: Each method or class must implement their own error handling using
                # TODO: try catch.
                # * NOTE: If you want you can import LogHandler() from utilities/handler
                # * To log events.

                try:
                    # Recognize speech using Google Speech Recognition.
                    voice_input_value: Any = self._recognizer.recognize_google(audio) # type: ignore
                    self._voice_input = voice_input_value

                    print(f"{voice_input_recognized_message, voice_input_value}\n")
                    self._text_to_speech_handler.create_text_to_speech_announcer(
                        text_to_produce_speech=(
                            f"{voice_input_recognized_message, voice_input_value}"))

                    if voice_input_value in wake_words:
                        self._text_to_speech_handler.create_text_to_speech_announcer(
                    text_to_produce_speech=random_greeting)

                except UnknownValueError:
                    print(could_not_recognize_voice_input_message)
                    self._text_to_speech_handler.create_text_to_speech_announcer(
                        text_to_produce_speech=could_not_recognize_voice_input_message)

                except RequestError as err:
                    print(f"{request_error_message_for_google_speech_recognition, err}")
                    self._text_to_speech_handler.create_text_to_speech_announcer(
                        text_to_produce_speech=(
                            request_error_message_for_google_speech_recognition))
                    return None

        except KeyboardInterrupt:
            print("Dear user, you have entered \"ctrl+c\", hence the program has been terminated.")
            self._text_to_speech_handler.create_text_to_speech_announcer(
                text_to_produce_speech=(
                    "Dear user, you have terminated the program by pressing the "
                    "control key with the letter C key available on your keyboard. "
                    "Good Bye and Take Care"))

        return self._voice_input
