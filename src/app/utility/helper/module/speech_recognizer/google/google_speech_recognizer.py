"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

google_speech_recognizer.py:
============================
This file contains a method that recognizes speech using Google Speech Recognition.

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

# Include built-in types.
import sys

# Include internal typings.
from typing import Any

# Include external packages and modules.
from speech_recognition import UnknownValueError, RequestError # type: ignore

def google_speech_recognizer(recognizer: Any, audio: Any,
        text_to_speech_handler: Any, **kwargs: str) -> str:
    """Recognizes speech using Google Speech Recognition.

    Args:
        - recognizer (Any): The recognizer object used for speech recognition.
        - audio (Any): The audio input to be recognized.
        - text_to_speech_handler (Any): The handler for converting text to speech.

    Kwargs (str): Keyword arguments for customization:
        - voice_input_recognized_message (str): Custom message when voice input is recognized.
        - could_not_recognize_voice_input_message (str):
        Custom message when voice input cannot be recognized.
        - request_error_message_for_google_speech_recognition (str):
        Custom message for Google Speech Recognition request errors.

    Returns:
        str: The recognized voice input as a string.

    Note:
        - The function uses the `recognizer` object to recognize speech from the `audio` input.
        - Audio input comes from the `SpeechRecognition` library.
        - Customization of messages can be done through keyword arguments in **kwargs.
    """

    # Define announcement messages.
    voice_input_recognized_message: str = kwargs.get(
        "voice_input_recognized_message", "")

    could_not_recognize_voice_input_message: str = kwargs.get(
        "could_not_recognize_voice_input_message", "")

    request_error_message_for_google_speech_recognition: str = (
        "\nDear user! you will not be able to use google speech recognition as you are offline.\n"
        "Please turn on your internet to access Google's speech recognition.")

    voice_input: str = "(Google Speech Recognition was not able to understand the speech)\n"

    try:
        # Recognize speech using Google Speech Recognition.
        voice_input = recognizer.recognize_google(audio) # type: ignore

        print(f"{voice_input_recognized_message, voice_input}\n")
        text_to_speech_handler.create_text_to_speech_announcer(
            text_to_produce_speech=(
                f"{voice_input_recognized_message, voice_input}"))

    except UnknownValueError:
        print(could_not_recognize_voice_input_message)
        text_to_speech_handler.create_text_to_speech_announcer(
            text_to_produce_speech=could_not_recognize_voice_input_message)

    except RequestError:
        print(request_error_message_for_google_speech_recognition)
        text_to_speech_handler.create_text_to_speech_announcer(
            text_to_produce_speech=(
                request_error_message_for_google_speech_recognition))
        sys.exit()

    return voice_input
