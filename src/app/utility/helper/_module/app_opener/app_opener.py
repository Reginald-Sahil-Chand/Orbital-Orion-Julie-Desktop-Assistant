"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

app_opener.py:
==============
This file contains a function that is responsible to open applications based on the given query.

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
from typing import Any, List

# Include external packages and modules.
from AppOpener import open as open_app, give_appnames # type: ignore


class AppNotFoundError(Exception):
    """Handle app not found error."""

def open_application(query: str, text_to_speech_handler: Any) -> None:
    """Opens an application based on the provided query using AppOpener.

    Args:
        - query (str): The user query specifying the application to open.
        - text_to_speech_handler (Any): The text-to-speech handler for generating speech output.

    Returns:
        - None.

    Raises:
        - Exception: If an error occurs during the application opening process.
    """

    app_names: Any = give_appnames(upper=False)

    _split_query_into_words: List[str] = query.split()[1::]
    _queried_application_name: str = " ".join(_split_query_into_words)

    _app_not_found_error: str =(
         "The requested application is not found in your device. Please try again!")

    try:
        # * open_app(_queried_application_name, match_closest=True, throw_error=True)
        # I actually dont use this because sometimes it gives weird results.
        # * Example: if the query = cloud -> Microsoft clock (if available in your device)
        # * will be opened.
        open_app(_queried_application_name,
                 match_closest=False,
                 output=False,
                 throw_error=True)

        if _queried_application_name.strip():
            if _queried_application_name in app_names:
                text_to_speech_handler.create_text_to_speech(
                                text_to_produce_speech=(
                                    f"{_queried_application_name} has been opened."))

            else:
                _app_not_found_error = (
                    f"{_queried_application_name} is not found in your device. Please try again!")

                text_to_speech_handler.create_text_to_speech(
                    text_to_produce_speech=_app_not_found_error)

        else:
            text_to_speech_handler.create_text_to_speech(
                text_to_produce_speech=_app_not_found_error)

    except AppNotFoundError:
        # We only speak the exception if "Speech Recognition" is not in the,
        # queried application name, because if the queried application name is empty,
        # then speech_recognizer will handle those errors.
        if "Speech Recognition" not in _queried_application_name:
            text_to_speech_handler.create_text_to_speech(
                                text_to_produce_speech=_app_not_found_error)
