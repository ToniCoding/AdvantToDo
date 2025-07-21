"""
This module defines the class `TaskCenterIntf` which provides the interface and function calls for the task center.

Dependencies:
- `check_if_integer` from `tools.strTools` for input validation.
- `Logger` from `tools.logger` for logging.
- `MenuController` from `modules.controller.MenuController` for menu management.

Class:
    TaskCenterIntf: Class that provides the interface and function calls for the task center.

Methods:
    __init__(self) -> None:
        Initializes the `TaskCenterIntf` class.

    task_center_menu(self) -> str:
        Returns the task center menu as a string.

    handle_task_center_action(self, task_controller: object) -> bool:
        Handles user actions in the task center.
"""

from os import system
from tools.strTools import check_if_integer
from tools.logger import Logger
from modules.controller.MenuController import MenuController

log = Logger("log/program.log")
menu_controller = MenuController()

class TaskCenterIntf:
    """
    Class that provides the interface and function calls for the task center.

    Methods:
        __init__(self) -> None:
            Initializes the class without arguments.

        task_center_menu(self) -> str:
            Returns the task center menu as a string.

        handle_task_center_action(self, task_controller: object) -> bool:
            Handles user actions in the task center.
    """
    
    def __init__(self):
        """
        Initializes the `TaskCenterIntf` class. This constructor takes no parameters and performs no actions.
        """
        pass

    def task_center_menu(self) -> str:
        """
        Returns the task center menu as a string.

        Uses `MenuController` to generate the menu from a file.

        Returns:
        str: The task center menu.
        """
        return menu_controller.generate_step_menu("./tx/english/task_center_menu.txt")

    def handle_task_center_action(self, task_controller: object) -> bool:
        """
        Handles user actions in the task center.

        Prompts the user for a selection and executes the corresponding task action.

        Parameters:
        task_controller (object): The task controller object to manage tasks.

        Returns:
        bool: True if the action was successfully executed, False if invalid option is selected or user wants to leave the interface or program.

        Logs:
        Logs information and errors based on user actions and input validation.
        """
        user_selection = input("Selection: ")

        if not check_if_integer(user_selection):
            raise ValueError
        
        try:
            user_selection = int(user_selection)

            match user_selection:
                case 1:
                    log.info("[TASK_INTF] Executed the registration of a task.")

                    if (task_controller.register_task()):  # type: ignore
                        print("Successfully registered new task!\n")
                        log.info("[TASK_INTF] Successfully registered new task.")
                    return True

                case 2:
                    log.info("[TASK_INTF] Executed view all tasks.")
                    task_controller.view_task() # type: ignore
                    return True

                case 3:
                    log.info("[TASK_INTF] Executed view specific task.")
                    return True

                case 4:
                    log.info("[TASK_INTF] Executed edit task.")
                    return True

                case 5:
                    log.info("[TASK_INTF] Executed delete task.")
                    task_controller.delete_task(int(input("ID of task to delete: ")))  # type: ignore
                    return True

                case 6:
                    log.info("[TASK_INTF] Executed exit task center interface.")
                    return False

                case 7:
                    log.info("[TASK_INTF] Executed exit program from task center interface.")
                    exit("Exiting program...")
                    return False

                case _:
                    log.err("[TASK_INTF] Operation not recognized.")
                    return False
        
        except FileNotFoundError:
            log.warn("[TASK_INTF] File with registered tasks is not created yet this month. Probably due to a change of the user's month.")
            print("No task was registered this month.")

            return False

        except ValueError as VE:
            log.err(f"[TASK_INTF] The prompted value is not an integer.")
            return False

        except Exception as e:
            log.err(f"[TASK_INTF] An unhandled exception happened: {e}")
            return False
                