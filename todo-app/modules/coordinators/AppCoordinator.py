"""
This module defines the class `AppCoordinator` which coordinates the application flow and user interactions.

Dependencies:
- `show_software_info`, `show_about_me`, `show_socials` from `tools.software_info` for displaying software information.
- `TaskCenterIntf` from `modules.interfaces.task_center_intf` for task center interactions.

Class:
    AppCoordinator: Class that coordinates the application flow and user interactions.

Methods:
    __init__(self, menu_controller: object, task_controller: object) -> None:
        Initializes the `AppCoordinator` class with controllers.

    runApplication(self) -> None:
        Runs the main application loop.

    print_menu(self) -> int:
        Prints the menu and returns the user's choice.

    handle_user_choice(self, user_option: int) -> bool:
        Handles the user's menu choice and executes corresponding actions.
"""

from os import system
from tools.software_info import show_software_info, show_about_me, show_socials
from tools.logger import Logger
from modules.interfaces.TaskCenterIntf import TaskCenterIntf

task_center_intf = TaskCenterIntf()
log = Logger("log/program.log")

class AppCoordinator:
    """
    Class that coordinates the application flow and user interactions.

    Methods:
        __init__(self, menu_controller: object, task_controller: object) -> None:
            Initializes the class with controllers.

        runApplication(self) -> None:
            Runs the main application loop.

        print_menu(self) -> int:
            Prints the menu and returns the user's choice.

        handle_user_choice(self, user_option: int) -> bool:
            Handles the user's menu choice and executes corresponding actions.
    """
    
    def __init__(self, menu_controller: object, task_controller: object):
        """
        Initializes the `AppCoordinator` class with controllers.

        Parameters:
        menu_controller (object): The menu controller object.
        task_controller (object): The task controller object.
        """
        self.menu_controller = menu_controller
        self.task_controller = task_controller

    def runApplication(self):
        """
        Runs the main application loop.

        Continuously runs the application, displaying the menu and handling user choices.
        """
        log.info("[APP_COORDINATOR] Program start executed successfully.")
        user_selection = self.print_menu()
        system("clear")
        self.handle_user_choice(user_selection)

    def print_menu(self) -> int:
        """
        Prints the menu and returns the user's choice.

        Returns:
        int: The user's menu choice.
        """
        return self.menu_controller.print_menu_with_choice() # type: ignore
    
    def run_task_center_intf(self) -> None:
        while True:
            print(task_center_intf.task_center_menu())
            
            if not task_center_intf.handle_task_center_action(self.task_controller):
                break

    def handle_user_choice(self, user_option: int) -> bool:
        """
        Handles the user's menu choice and executes corresponding actions.

        Parameters:
        user_option (int): The user's menu choice.

        Returns:
        bool: True if the action was successfully executed, False otherwise.

        Raises:
        ValueError: If the user's choice is not recognized.
        """

        try:
            if user_option == 1:
                self.run_task_center_intf()
                
                return True

            else:
                match user_option:
                    case 2:
                        log.info("[APP_COORDINATOR] Executed show_software_info function.")
                        show_software_info()
                        return True
                    case 3:
                        log.info("[APP_COORDINATOR] Executed show_about_me function.")
                        show_about_me()
                        return True
                    case 4:
                        log.info("[APP_COORDINATOR] Executed show_software_info function.")
                        show_socials()
                        return True
                    case 5:
                        log.info("[APP_COORDINATOR] Executed exit program function.")
                        exit("Exiting...")
                        return True
                    case _:
                        raise ValueError("The prompted value is not recognized.")
        
        except ValueError:
            print("Invalid option.\n")
            log.err("[APP_COORDINATOR] User selected an invalid option.")
            
            return False
        
        except Exception as e:
            print("An uncaught exception happened, check log for more information.")
            log.err(f"Uncaught exception happened: {e}")

            return False
