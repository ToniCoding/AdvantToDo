"""
This module provides functions to display software information and open social media links.

Dependencies:
- `webbrowser` for opening URLs in a web browser.

Functions:
    show_software_info() -> None:
        Displays information about the software.

    show_about_me() -> None:
        Displays information about the author.

    show_socials() -> None:
        Displays social media information and opens a GitHub profile if requested.
"""

from modules.helpers.JSONReader import JSONReader
from tabulate import tabulate
import webbrowser

json_config = JSONReader("config/app_config.json")
json_config_read = json_config.get_software_info()

def show_software_info() -> None:
    """
    Displays information about the software.
    """
    print(
f"""
Name: {json_config_read[0]}
Version: {json_config_read[1]}
Release date: {json_config_read[2]}
Author: {json_config_read[3]}
Description: {json_config_read[4]}
""")

def show_about_me() -> None:
    """
    Displays information about the author.
    """
    print("I'm Antonio. A self-taught software developer who is trying to advance in his professional career.\n")

def show_socials() -> None:
    """
    Displays social media information and opens a GitHub profile if requested.
    """
    print("Find me at GitHub.\n")
    if (input("Open ToniCoding's GitHub profile? (y/n): ").lower() == "y"):
        webbrowser.open_new_tab("https://github.com/ToniCoding")
