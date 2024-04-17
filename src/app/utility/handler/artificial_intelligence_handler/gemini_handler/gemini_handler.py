"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

gemini_handler.py:
==================
This file contains a class that communicates with, Google's Gemini API,
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

# * NOTE: "# type: ignore" has been used at some places because, some packages,
# * Does not have a specific stub file hence pylint / pylance are unable to infer types.
# * Thus to avoid unnecessary errors and warnings, making the code base noisy, I decided to,
# * Ignore types for some parts of the code.

# Include built-in packages and modules.
from dataclasses import dataclass

# Include external packages and modules.
import google.generativeai as genai # type: ignore

# Configure API KEY
genai.configure(api_key="YOUR_API_KEY") # type: ignore


@dataclass
class GeminiHandler:
    """This file contains a class that communicates with, Google's Gemini API.

    - Initiate the class.
    - Get the voice or text input as text to feed the AI.
    - Generate the response based on the given input.
    - Return back the generated response.
    """

    # Choose which AI/LLM model to use.
    _model = genai.GenerativeModel('gemini-pro')

    # Store Gemini's response.
    _models_response: str = (
        "Gemini AI (GEMINI-PRO) was unable to process your response. Please Try Again.")

    def initiate_gemini_ai(self, prompt: str) -> str:
        """Initiate the Gemini AI model with the given prompt and return the generated response.

        Args:
           - prompt (str): The input prompt for the AI model.

        Returns:
            - str: The generated response from the AI model.
        """

        try:
            # Feed the given prompt to the model.
            response: genai.GenerativeModel = self._model.generate_content( # type: ignore
                f"\"{prompt}\"")

            # Store the response in a separate variable to return later.
            self._models_response: str = str(response.text) # type: ignore

        except ValueError as err:
            print(f"An error occurred: {err}")

        return self._models_response
