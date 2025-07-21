"""
This module defines the class `MenuModel` which provides methods to retrieve menu options from a file.

Dependencies:
- `FileHandler` from `tools.FileHandler` for file operations.

Class:
    MenuModel: Class that provides methods to retrieve menu options.

Methods:
    __init__(self) -> None:
        Initializes the `MenuModel` class.

    get_menu_options(self, options_file: str, lang: str = "eng") -> str:
        Retrieves menu options from a specified file.
"""

from tools.FileHandler import FileHandler

file_handler = FileHandler("READ_FILE")

class MenuModel:
    """
    Class that provides methods to retrieve menu options.

    Methods:
        __init__(self) -> None:
            Initializes the class without arguments.

        get_menu_options(self, options_file: str, lang: str = "eng") -> str:
            Retrieves menu options from a specified file.
    """
    
    def __init__(self):
        """
        Initializes the `MenuModel` class. This constructor takes no parameters and performs no actions.
        """
        pass

    def get_menu_options(self, options_file: str, lang: str = "eng") -> str:
        """
        Retrieves menu options from a specified file.

        Parameters:
        options_file (str): The path to the file containing menu options.
        lang (str): The language of the menu options. Default is "eng".

        Returns:
        str: The content of the menu options file.
        """
        options_content = file_handler.read_file(options_file)
        
        return options_content
