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

# Include external packages and modules.
import google.generativeai as genai # type: ignore


@dataclass
class GeminiAi:
    """This file contains a class that communicates with, Google's Gemini AI API.

    - Initiate the class.
    - Get the voice or text input as text to feed the AI.
    - Generate the response based on the given input.
    - Return back the generated response.
    """

    # Choose which AI/LLM model to use.
    _model = genai.GenerativeModel('gemini-pro')

    _model_response: str = ""

    # * Display this error message in the console if you want to. (Use this in exceptions).
    _universal_error_message: str = (
        "Could not communicate with GEMINI AI. Some error occurred. Please try Again!")

    def initiate_gemini_ai(self, prompt: str) -> str:
        """Initiate the Gemini AI model with the given prompt and return the generated response.

        Args:
           - prompt (str): The query prompt for the AI model.

        Returns:
            - str: The generated response from the AI model.
        """

        try:
            if prompt.strip():
                # Feed the given prompt to the model.
                response: genai.GenerativeModel = self._model.generate_content( # type: ignore
                f"\"{prompt}\"")

                # Store the response in a separate variable to return later.
                self._model_response: str = str(response.text) # type: ignore

        except Exception:
            pass

        return self._model_response
