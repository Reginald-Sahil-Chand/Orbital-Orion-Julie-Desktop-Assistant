"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

initiate_julie.py:
==================
This file contains a function to initiate julie.

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
import sys

# Include internal typings.
from typing import Any

# Include custom packages and modules.
from src.app.utility.data._module.wake_words import wake_words_to_self_describe,\
    wake_words_to_exit_program
from src.app.utility.helper._module.app_opener.app_opener import open_application
from src.app.home._class.start.sr_ware_house._internals.ai import initiate_gemini_ai


def initiate_julie(speech_recognizer: str,
                   set_speech_recognizer: Any,
                   text_to_speech_handler: Any,
                   gemini_handler: Any) -> None:
    """Initiates awakening of Julie to perform tasks.

    Args:
        - speech_recognizer (str): The type of speech recognizer to use for waking up Julie.
        - set_speech_recognizer (Any): The set_speech_recognizer object to be used for the
        awakening process.
        - text_to_speech_handler (Any): The text_to_speech_handler object to be used for
        speaking text.
        - gemini_handler (Any): The gemini_handler object to be used for generating ai response.

    Returns: 
        - None.
    """

    while True:
        query = set_speech_recognizer.initiate_speech_recognition(
            speech_recognizer=speech_recognizer)

        if (query in f"open {query[5::]}" or query in f"go to {query[6::]}"):
            open_application(query=query,
                text_to_speech_handler=text_to_speech_handler)

        elif query in wake_words_to_self_describe:
            text_to_speech_handler.create_text_to_speech(
                text_to_produce_speech=(
                    "I'm Julie, a desktop assistant created by Reginald Chand!"
                    "He created me as a personal project."))

        elif query in wake_words_to_exit_program:
            text_to_speech_handler.create_text_to_speech(
                text_to_produce_speech=(
                    "Thank you for using my service. Exiting Program. Take Care!"))
            sys.exit(0)

        else:
            initiate_gemini_ai.initiate_gemini_ai(query=query,
                      gemini_handler=gemini_handler,
                      text_to_speech_handler=text_to_speech_handler)
