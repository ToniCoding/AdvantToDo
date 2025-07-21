"""
This module defines the class `MenuController` which provides methods to generate and display a menu.

Dependencies:
- `MenuModel` from `modules.model.MenuModel` for menu data handling.
- `Logger` from `tools.logger` for logging.
- `check_if_integer` from `tools.strTools` for input validation.

Class:
    MenuController: Class that provides methods to generate and display a menu.

Methods:
    generate_step_menu(self, steps_path: str) -> str:
        Generates a step-by-step menu from a file.

    print_menu_with_choice(self) -> int:
        Displays the menu and prompts the user for a choice.
"""

from modules.model.MenuModel import MenuModel
from tools.logger import Logger
from tools.strTools import check_if_integer

menu_model = MenuModel()
log = Logger("log/program.log")

class MenuController:
    """
    Class that provides methods to generate and display a menu.

    Methods:
        generate_step_menu(self, steps_path: str) -> str:
            Generates a step-by-step menu from a file.

        print_menu_with_choice(self) -> int:
            Displays the menu and prompts the user for a choice.
    """
    
    def generate_step_menu(self, steps_path: str) -> str:
        """
        Generates a step-by-step menu from a file.

        Parameters:
        steps_path (str): The path to the file containing menu options.

        Returns:
        str: A formatted string representing the menu.

        Raises:
        Exception: If the menu components are empty.
        """
        steps_content = menu_model.get_menu_options(steps_path)
        steps_txt_processed = steps_content.split(",", maxsplit=15)
        final_menu = ""
        step_iteration = 0

        if len(steps_txt_processed) == 1:
            raise Exception("Menu components are empty.")

        for step in steps_txt_processed:
            step_iteration += 1
            final_menu += f"{step_iteration}. {step.capitalize()}.\n"

        return final_menu
    
    def print_menu_with_choice(self) -> int:
        """
        Displays the menu and prompts the user for a choice.

        Prints the generated menu and asks the user to select an option.
        Validates if the user's input is an integer.

        Returns:
        int: The user's choice as an integer.
        """
        print(self.generate_step_menu("./tx/english/menu.txt"))

        user_choice = input("Selection: ")

        if check_if_integer(user_choice):
            return int(user_choice)
        
        return -1
