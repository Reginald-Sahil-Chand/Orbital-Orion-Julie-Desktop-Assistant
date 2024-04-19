"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

init.py:
========
This file contains Google's GEMINI AI API KEY which must be provided in order to use,
GEMINI AI Service.

LINK TO GET AN API KEY: https://aistudio.google.com/app

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

# Include external packages and modules.
import google.generativeai as genai # type: ignore


# * LINK TO GET AN API KEY: https://aistudio.google.com/app
genai.configure(api_key="YOUR_API_KEY") # type: ignore
