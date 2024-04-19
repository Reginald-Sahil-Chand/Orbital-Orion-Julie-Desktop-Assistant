"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

google_speech_recognizer.py:
============================
This file contains a function that recognizes speech using Google Speech Recognition.

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

# Include internal typings.
from typing import Any

# Include external packages and modules.
from speech_recognition import AudioData, UnknownValueError, RequestError # type: ignore


def google_speech_recognizer(recognizer: Any,
                             audio: AudioData,
                             text_to_speech_handler: Any,
                             should_announce_error_message: bool) -> str:
    """Recognizes speech using Google Speech Recognition.

    Args:
        - recognizer (Any): The recognizer object used for speech recognition.
        - audio (Any): The audio input to be recognized.
        - text_to_speech_handler (Any): The handler for converting text to speech.
        - should_announce_error_message (str): To control the flow of error messages.

    Returns:
        - str: The recognized voice input as a string.

    Raises:
        - Exception: if query is empty or not understood.
        - Exception: if the user is offline.

    Note:
        - The function uses the `recognizer` object to recognize speech from the `audio` input.
        - Audio input comes from the `SpeechRecognition` library.
    """

    _unknown_value_error_message: str = (
        "Sorry, I didn't catch that. Could you please rephrase or clarify your question?\n")

    _request_error_message: str = (
        "Oops! It seems there's an issue with your connection.\n"
        "Please check your internet settings and try again for voice "
        "recognition to work smoothly.\n")

    _query: str = ""

    try:
        _query = recognizer.recognize_google(audio)

    except UnknownValueError:
        if should_announce_error_message:
            text_to_speech_handler.create_text_to_speech(
                text_to_produce_speech=_unknown_value_error_message)

    except RequestError:
        text_to_speech_handler.create_text_to_speech(
            text_to_produce_speech=_request_error_message)

    return _query
