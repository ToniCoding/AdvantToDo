"""
This module defines the class `Logger` which provides methods for logging messages with different severity levels.

Dependencies:
- `datetime` from `datetime` for timestamping log entries.
- `Enum` from `enum` for defining log modes.

Class:
    Logger: Class that provides methods for logging messages.

Methods:
    __init__(self, logPath: str) -> None:
        Initializes the `Logger` class with a log file path.

    __write_log(self, logMode: str, logMsg: str) -> bool:
        Writes a formatted log message to the log file.

    info(self, msg: str) -> None:
        Logs an information message.

    sys(self, msg: str) -> None:
        Logs a system message.

    warn(self, msg: str) -> None:
        Logs a warning message.

    err(self, msg: str) -> None:
        Logs an error message.
"""

from datetime import datetime
from enum import Enum

class Logger:
    """
    Class that provides methods for logging messages with different severity levels.

    Methods:
        __init__(self, logPath: str) -> None:
            Initializes the class with a log file path.

        __write_log(self, logMode: str, logMsg: str) -> bool:
            Writes a formatted log message to the log file.

        info(self, msg: str) -> None:
            Logs an information message.

        sys(self, msg: str) -> None:
            Logs a system message.

        warn(self, msg: str) -> None:
            Logs a warning message.

        err(self, msg: str) -> None:
            Logs an error message.
    """
    
    def __init__(self, logPath: str) -> None:
        """
        Initializes the `Logger` class with a log file path. This ensures the file is created if it's deleted or is not created yet.

        Parameters:
        logPath (str): The path to the log file.
        """
        self.logPath = logPath

        with open(self.logPath, "a") as _:
            pass

    class LoggerMode(Enum):
        """ This class will be in charge of the logging states such as information, warning, errors """
        SYSTEM = "SYS"
        INFORMATION = "INFO"
        WARNING = "WARN"
        ERROR = "ERR"
    
    def __write_log(self, logMode: str, logMsg: str) -> bool:
        """
        Writes a formatted log message to the log file.

        Parameters:
        logMode (str): The mode of the log (e.g., INFO, WARN).
        logMsg (str): The message to log.

        Returns:
        bool: True if the log was written successfully, False otherwise.
        """
        formatted_date = datetime.now().strftime("%d-%m-%YT%H:%M:%S,%f")[:-3]
        logLine = f"[{logMode}]{formatted_date} - {logMsg}"

        write_to_log = open(self.logPath, "+a").write(logLine)

        return True if write_to_log else False

    def info(self, msg: str) -> None:
        """ Logs an information message """
        self.__write_log(self.LoggerMode["INFORMATION"].value, f"{msg}\n")
    
    def sys(self, msg: str) -> None:
        """ Logs a system message """
        self.__write_log(self.LoggerMode["SYSTEM"].value, f"{msg}\n")
    
    def warn(self, msg: str) -> None:
        """ Logs a warning message """
        self.__write_log(self.LoggerMode["WARNING"].value, f"{msg}\n")
    
    def err(self, msg: str) -> None:
        """ Logs an error message. """
        self.__write_log(self.LoggerMode["ERROR"].value, f"{msg}\n")
