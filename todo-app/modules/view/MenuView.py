"""
This module defines the class `MenuView` which provides methods to display a menu with decorative lines.

Class:
    MenuView: Class that provides methods to display a menu.

Methods:
    __init__(self) -> None:
        Initializes the `MenuView` class.

    print_menu(self, menu_content: str) -> str:
        Returns a formatted string representing the visual menu.
"""

class MenuView:
    """
    Class that provides methods to display a menu with decorative lines.

    Methods:
        __init__(self) -> None:
            Initializes the class without arguments.

        print_menu(self, menu_content: str) -> str:
            Returns a formatted string representing the visual menu.
    """
    
    LINE_DECORATOR_1 = "-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-"
    LINE_DECORATOR_2 = "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    LINE_DECORATOR_3 = "/////////////////////////////////////////////////////////////"
    LINE_DECORATOR_4 = "#############################################################"

    def __init__(self):
        """
        Initializes the `MenuView` class. This constructor takes no parameters and performs no actions.
        """
        pass

    def print_menu(self, menu_content: str) -> str:
        """
        Returns a formatted string representing the visual menu.

        Parameters:
        menu_content (str): The content of the menu to be displayed.

        Returns:
        str: A formatted string with decorative lines and menu content.
        """
        visual_menu = f"{self.LINE_DECORATOR_2}\nToDo Agenda --- Created by ToniCoding --- Python scripting\n{menu_content}{self.LINE_DECORATOR_2}"
        
        return visual_menu
