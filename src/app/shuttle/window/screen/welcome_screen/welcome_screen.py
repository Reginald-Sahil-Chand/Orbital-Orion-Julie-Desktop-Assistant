"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

welcome_screen.py:
==================
Displays a welcome message when the program starts.

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


@dataclass(frozen=True)
class WelcomeScreen:
    """Class to initiate the welcome screen creation."""

    @staticmethod
    def create_welcome_screen() -> None:
        """Creates a welcome screen and display the welcome message.
        
        Returns None
        """

        _welcome_message: str = r"""
 __        _______ _     ____ ___  __  __ _____   _____ ___     ___   ___      _ ____    _    
 \ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \   / _ \ / _ \    | |  _ \  / \   
  \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | | | | | | | | |_  | | | | |/ _ \  
   \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| | | |_| | |_| | |_| | |_| / ___ \ 
    \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/   \___/ \___/ \___/|____/_/   \_\
                                                  
"""

        print(_welcome_message,
              "\n\t\t\t====> ORBITAL ORION'S JULIE DESKTOP ASSISTANT <====\n")
