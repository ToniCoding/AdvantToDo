""" This file is in charge of having some utility functions related to dates and time """

from datetime import datetime

def getDateDetails(details_requested: str) -> list:
    """
    Returns a list with the date details the user have requested.

    Parameters:
    details_requested(str): The details the user will need. Can be combined.
        - m: Month.
        - y: Year.
        - d: Day.

    Returns:
    date_details(list): A list of the details requested by the user.
    """
    
    current_date = datetime.now()
    valid_details = ("m", "y", "d")
    details_list = list(details_requested)
    date_details = []
    
    for detail in details_list:
        
        if (detail not in valid_details):
            raise ValueError(f"The detail {detail} is not valid.")

        match detail:
            case "d":
                date_details.append(current_date.day)
            
            case "m":
                date_details.append(current_date.month)

            case "y":
                date_details.append(current_date.year)
            
            case _:
                print("No available data.")

    return date_details

def monthTranslator(month: int, month_format: str = "short") -> str:
    """
    Returns the month expressed in words.

    Parameters:
    month (int): The month to be translated (1 for January, 12 for December).
    month_format (str): The format of the translated month.
        - "short": Will return 3-letter month abbreviation.
        - "long": Will return the full month name.

    Returns:
    month (str): The month translated.

    Raises:
    ValueError: If the month is not between 1 and 12 or if the month_format is not recognized.
    """
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12.")

    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

    match month_format.lower():
        case "short":
            return months[month][0:3]
        
        case "long":
            return months[month][0:3]
        
        case _:
            raise ValueError("Month format must be 'short' or 'long'.")

def isDateFormattedCorrectly(date: str) -> bool:
    """
        Checks if the date is formatted correctly as DD_MM_YYYY.

        Parameters:
        date (str): The date string to check.

        Returns:
        bool: True if the date is formatted correctly, False otherwise.
    """
    try:
        day, month, year = map(int, date.split("_"))

        datetime(year, month, day)
        return True
    except (ValueError, TypeError):
        return False
