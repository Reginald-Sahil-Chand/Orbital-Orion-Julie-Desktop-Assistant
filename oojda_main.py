"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

oojda_main.py:
==============
Controls the execution of the overall software.
Can be referred to as the entry point for the Orbital Orion - Julie Desktop Assistant.

Overview:
=========
Initiating Orbital Orion's - Julie Desktop Assistant's Launch Process 🚀

This script serves as the launchpad for our software.
Executing start_engine_oojda_main() will ignite the program and commence our cosmic exploration.

Usage:
======
This module consists of one function named start_engine_oojda_main.
This function as the name suggests is responsible to start the main program flow.

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

# Include custom packages and modules.
from src.app.home._class.oojda_control_panel.oojda_control_panel import OojdaControlPanel
from src.app.utility.handler._class.log_handler.log_handler import LogHandler

# Include Metadata.
__author__ = "Reginald Sahil Chand"
__maintainer__ = "ReginaldSahilChand"
__credits__ = "Reginald Sahil Chand"
__email__ = "Developer.ReginaldSahilChand@gmail.com"

__version__ = "0.1.0"
__license__ = "General Public License Version 3.0"
__copyright__ = "Copyright 2024, Reginald Sahil Chand"

__status__ = "Development"


def start_engine_oojda_main() -> None:
    """Start the main program flow.

    Initialize:
    - oojda_controller.initiate_oojda_launch_sequence()
    - oojda_controller.initiate_oojda_launch_service()
    - This initialization will allow this whole software to operate smoothly.

    Note:
    - This function does not and must not take any arguments.
    - This function must also not return any value.
    
    Returns None
    """

    # Instantiate OojdaControlPanel.
    oojda_controller: OojdaControlPanel = OojdaControlPanel()

    # Instantiate LogHandler.
    log_handler: LogHandler = LogHandler()

    # Define error and warning messages.
    _system_error_message: str = "Alert, There has been a malfunction in the system: "
    _keyboard_interrupt_message: str = """Mission Abort: Orbital Orion's Desktop Assistant
Julie Has Been Terminated.
\nYou have entered Ctrl + C hence the program has terminated.
"""

    try:
        oojda_controller.initiate_oojda_launch_sequence()
        oojda_controller.initiate_oojda_launch_service()

    except SystemError as system_error:
        print(_system_error_message, system_error)
        log_handler.create_log(log_type="error",
                               log_message=f"{_system_error_message, system_error}")

    except KeyboardInterrupt:
        print(_keyboard_interrupt_message)
        log_handler.create_log(log_type="warning", log_message=_keyboard_interrupt_message)

    except SystemExit:
        log_handler.create_log(log_type="warning", log_message="System Exit")


if __name__ == "__main__":
    start_engine_oojda_main()
