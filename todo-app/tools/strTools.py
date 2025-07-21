"""
This module provides utility functions for string manipulation.

Functions:
    complyWithLen(string: str, max_len: int = 4) -> bool:
        Checks if a string is N characters long or shorter.

    replace_special_chars_with_underscore(input_string: str) -> str:
        Replaces special characters with underscores.

    translate_date_to_legible(date_input: str) -> str:
        Translates a converted date to a human-readable format.

    check_if_integer(user_input: str) -> bool:
        Checks if the argument is an integer.

    list_to_string(list_to_convert: list) -> str:
        Converts a list into a full string.
"""

from re import sub

def complyWithLen(string: str, max_len: int = 4) -> bool:
    """
    Checks if a string is N characters long or shorter.

    Parameters:
    string (str): The string to check.
    max_len (int): The maximum length allowed.

    Returns:
    bool: True if the string is within the length limit, False otherwise.
    """
    return len(string) <= max_len

def replace_special_chars_with_underscore(input_string: str) -> str:
    """
    Replaces special characters with underscores. This is mostly used for date processing.

    Parameters:
    input_string (str): The string to process.

    Returns:
    str: The processed string with special characters replaced.
    """
    pattern = r'[-/]'
    result = sub(pattern, '_', input_string)
    return result

def translate_date_to_legible(date_input: str) -> str:
    """
    Translates a converted date to a human-readable format.

    Parameters:
    date_input (str): The date string to translate.

    Returns:
    str: The translated date string.
    """
    translated_date = date_input.replace("_", "/")
    return translated_date

def check_if_integer(user_input: str) -> bool:
    """
    Checks if the argument is an integer.

    Parameters:
    user_input (str): The input to check.

    Returns:
    bool: True if the input is an integer, False otherwise.
    """
    try:
        int(user_input)
        return True
    except ValueError:
        return False
    
def list_to_string(list_to_convert: list) -> str:
    """
    Converts a list into a full string.

    Parameters:
    list_to_convert (list): The list to convert.

    Returns:
    str: The concatenated string.
    """
    converted_string = ""
    for list_element in list_to_convert:
        converted_string += list_element
    return converted_string

def remove_initial_spaces_from_string(string_to_convert: str) -> str:
    splitted_string = list(string_to_convert)
    converted_string = ""

    for i, char in enumerate(splitted_string):
        if char != " ":
            converted_string = "".join(splitted_string[i:])
            break

    return converted_string

