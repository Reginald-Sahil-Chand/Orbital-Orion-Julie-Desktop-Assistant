"""
Fun Fact:
=========
This software is based on a space theme.
All the functions, variables, and class names used are meaningful and follows a space theme.
This codebase will consist of comments based on humors at minimum to cheer up other developers.

notification_handler.py:
========================
Class to handle desktop notifications.

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
from plyer import notification # type: ignore


@dataclass
class NotificationHandler:
    """Class to handle desktop notifications."""

    @staticmethod
    def create_notification(title: str, message: str, app_name: str,
                            timeout: int) -> None:
        """Method to create desktop notifications.

        Args:
            - title (str): The notification title.
            - message (str): The notification message to inform to the users.
            - app_name (str): The name of the software toasting the notification.
            - timeout (str): How many minutes or seconds the notification should be shown.
        
        Returns:
            - None
        """

        notification.notify(title=title, message=message,
                            app_name=app_name,
                            timeout=timeout) # type: ignore
