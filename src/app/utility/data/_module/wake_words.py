"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

wake_words.py:
==============
This file contains all wake words that will be used to activate the desktop assistant.
Also this is the module which has wake words that will be used to perform certain tasks,
given the condition.

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
from typing import Dict, Tuple


wake_words_to_activate_julie: Tuple[str, ...] = (
    "hi julie", "hi oojda", "hi orbital orion julie desktop assistant",
    "hey julie", "hey oojda", "hey orbital orion julie desktop assistant",
    "hello julie", "hello oojda", "hello orbital orion julie desktop assistant",
    "ok julie", "ok oojda", "ok orbital orion julie desktop assistant",
)

wake_words_to_open_apps: Dict[str, str] = {
        "wake_with_open": "",
        "wake_with_go_to": "",
    }

wake_words_to_self_describe: Tuple[str, ...] = (
    "who are you", "tell me about yourself", "tell me about yourself"
)
