"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

oojda_control_panel.py:
=======================
Controls initialization for two oojda components.
[1] = oojda_launch_sequencer which houses all the packages, functions, modules in the sequence
it needs to be executed.
[2] = oojda_launch_service which houses all the services it needs to be run in the background.

Overview:
=========
Initiating Orbital Orion's - Julie Desktop Assistant's Launch Sequence Process 🚀
Initiating Orbital Orion's - Julie Desktop Assistant's Launch Service Process 🚀

This script serves as the launch sequencer and servicer starting point for our software.

Usage:
======
This class consists of two static methods named
initiate_oojda_launch_sequence and initiate_oojda_launch_service will be responsible to invoke
the required classes.

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

# Include custom packages and modules.
from src.app.utility.handler._class.notification_handler.notification_handler\
    import NotificationHandler
from src.app.home._class.screen.welcome_screen.welcome_screen import WelcomeScreen
from src.app.home._class.user_information.user_information import UserInformation
from src.app.home._class.start.sr_ware_house.sr_ware_house import SRWareHouse


@dataclass
class OojdaControlPanel:
    """Class to control the launch initiation for oojda_launch_sequence and oojda_launch_service.
    
    - This class houses 2 static methods:
    - initiate_oojda_launch_sequence.
    - initiate_oojda_launch_service.
    - Which are responsible to initiate the required packages and services.
    """

    @staticmethod
    def initiate_oojda_launch_sequence() -> None:
        """Initiate the launch sequence for all required packages, modules, and methods
        in sequence.

        - The sequence must not be changed to avoid unwanted behavior.
        - Remember do not play with the space shuttle launch sequencer in the middle of launch.
        """

        # Instantiate classes.
        notification_handler: NotificationHandler =  NotificationHandler()
        notification_handler.create_notification(
            title="Orbital Orion Julie Desktop Assistant",
            message="Running in background.",
            app_name="Orbital Orion Julie Desktop Assistant",
            timeout=10)

        welcome_screen: WelcomeScreen = WelcomeScreen()
        welcome_screen.create_welcome_screen()

        user_information: UserInformation = UserInformation()
        user_information.create_user_information()

        initiate_speech_recognition: SRWareHouse = SRWareHouse()
        initiate_speech_recognition.initiate_speech_recognition(
            speech_recognizer="google_speech_recognizer")

    @staticmethod
    def initiate_oojda_launch_service() -> None:
        """Currently no launch services are identified."""
