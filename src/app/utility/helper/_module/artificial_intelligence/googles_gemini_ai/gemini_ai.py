"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

gemini_ai.py:
=============
This file contains a class that communicates with, Google's Gemini AI API,
- Initiate the class.
- Get the voice or text input as text to feed the AI.
- Generate the response based on the given input.
- Return back the generated response.

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
from dataclasses import dataclass

# Include internal typings.
from typing import Any

# Include external packages and modules.
from google import generativeai as genai # type: ignore
from google.api_core import exceptions

# * LINK TO GET AN API KEY: https://aistudio.google.com/app
genai.configure(api_key="YOUR_API_KEY") # type: ignore

# Choose which AI/LLM model to use.
MODEL = genai.GenerativeModel('gemini-pro')


def initiate_gemini_ai(prompt: str, text_to_speech_handler: Any) -> None:
    """Initiate the Gemini AI model with the given prompt and produce the requested data.

    Args:
       - prompt (str): The query prompt for the AI model.
       - text_to_speech_handler (Any): The class to handle text to speech.

    Returns:
        - None.
    """

    try:
        if prompt.strip():
            # Feed the given prompt to the model.
            response: genai.GenerativeModel = MODEL.generate_content( # type: ignore
            f"\"{prompt}\"")

            # Store the response in a separate variable to return later.
            _model_response: str = str(response.text.replace("*", "")) # type: ignore

            print(f"WARNING: AI GENERATED CONTENT | CAN BE INCORRECT.\n\n{_model_response}\n")

            text_to_speech_handler.create_text_to_speech(
                text_to_produce_speech=_model_response)

        else:
            text_to_speech_handler.create_text_to_speech(
                        text_to_produce_speech=(
                            "Sorry! I cant help you with this. Please try something else!"))

    except exceptions.InvalidArgument:
        pass

    except exceptions.RetryError:
        pass

    except exceptions.BadRequest:
        pass

    except exceptions.BadGateway:
        pass

    except exceptions.Forbidden:
        pass

    except exceptions.GoogleAPIError:
        pass
