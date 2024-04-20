"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

initiate_gemini_ai.py:
======================
This file contains a function to initiate Google's Gemini AI.

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


def initiate_gemini_ai(query: str, gemini_handler: Any, text_to_speech_handler: Any) -> None:
    """Communicates with Google's Gemini AI.

    Args:
        - query (str): The question asked by the user.
        - gemini_handler (Any): The gemini_handler object to be used for generating ai response.
        - text_to_speech_handler (Any): The text_to_speech_handler object to be used for
        speaking text.

    FYI:
        - For API_KEY initialization -> REFER __init__.py
        - Folder Reference: src/app/utility/handler/_class/artificial_intelligence/googles_gemini_ai
        - To create an API -> REFER LINK TO GET AN API KEY: https://aistudio.google.com/app
    """

    # * USE ARTIFICIAL INTELLIGENCE (GOOGLE'S GEMINI).
    user_requested_prompt: str = (
        gemini_handler.initiate_gemini_ai(prompt=query))

    remove_asterisk_from_prompt = user_requested_prompt.replace("*", "")

    print(f"{remove_asterisk_from_prompt}\n")
    text_to_speech_handler.create_text_to_speech(
        text_to_produce_speech=remove_asterisk_from_prompt)

    if not user_requested_prompt.strip():
        text_to_speech_handler.create_text_to_speech(
                text_to_produce_speech=(
                       "Sorry! I cant help you with this. Please try something else!"))
