"""
This module defines the class `FileHandler` which provides methods for file operations.

Dependencies:
- `Enum` from `enum` for defining file operation modes.
- `contextmanager` from `contextlib` for managing file resources.
- `Generator`, `IO` from `typing` for type hinting.
- `isfile` from `os.path` for checking file existence.
- `Logger` from `tools.logger` for logging.

Class:
    FileHandler: Class that provides methods for file operations.

Methods:
    __init__(self, operating_mode: str) -> None:
        Initializes the `FileHandler` class with an operating mode.

    set_operating_mode(self, new_operating_mode: str) -> None:
        Sets a new operating mode.

    get_operating_mode(self) -> FileOperatingMode:
        Returns the current operating mode.

    open_file(self, path: str, mode: str) -> Generator[IO, None, None]:
        Opens a file with resource management.

    write_file(self, path: str, content: str, mode: str) -> bool:
        Writes content to a file with the selected mode.

    read_file(self, path: str) -> str | None:
        Reads a file and returns the content.
"""

from enum import Enum
from contextlib import contextmanager
from typing import Generator, IO
from os.path import isfile
from tools.logger import Logger

log = Logger("log/program.log")

class FileHandler:
    """
    Class that provides methods for file operations.

    Methods:
        __init__(self, operating_mode: str) -> None:
            Initializes the class with an operating mode.

        set_operating_mode(self, new_operating_mode: str) -> None:
            Sets a new operating mode.

        get_operating_mode(self) -> FileOperatingMode:
            Returns the current operating mode.

        open_file(self, path: str, mode: str) -> Generator[IO, None, None]:
            Opens a file with resource management.

        write_file(self, path: str, content: str) -> bool:
            Appends content to a file.

        read_file(self, path: str) -> str | None:
            Reads a file and returns the content.
    """
    
    class UnsupportedOperationError(Exception):
        """ Custom exception to announce that the introduced operation is unsupported """
        def __init__(self, message = "Operation not supported"):
            self.message = message
            super().__init__(self.message)

    class FileOperatingMode(Enum):
        """ This class serves as tracker for the current operator mode of the file handler """
        NONE = 0
        READ_FILE = 1
        WRITE_FILE = 2
        DELETE_FILE = 3
    
    def __init__(self, operating_mode: str):
        """
        Initializes the `FileHandler` class with an operating mode.

        Parameters:
        operating_mode (str): The initial operating mode.
        """
        self.operating_mode = self.FileOperatingMode[operating_mode]

    def set_operating_mode(self, new_operating_mode: str) -> None:
        """
        Sets a new operating mode.

        Parameters:
        new_operating_mode (str): The new operating mode.
        """
        self.operating_mode = self.FileOperatingMode[new_operating_mode]
    
    def get_operating_mode(self) -> FileOperatingMode:
        """
        Returns the current operating mode.

        Returns:
        FileOperatingMode: The current operating mode.
        """
        return self.operating_mode
    
    @contextmanager
    def open_file(self, path: str, mode: str) -> Generator[IO, None, None]:
        """
        Opens a file securing a correct resource management in case of an exception.

        Parameters:
        path(str): The path to the file that will be read.
        mode(str): The mode in which the file will be opened.

        Yields:
        An IO object opened in the specified mode.

        File will be automatically closed after exiting the 'with' statement in which the function will be used.
        """
        try:
            file = open(path, mode)
            yield file
        finally:
            file.close() # type: ignore --- REVISION - No se como puede estar desvinculada tras una instancia literal.

    def write_file(self, path: str, content: str, mode: str = "a") -> bool:
        """
        Appends content to a file in a specified path.

        Parameters:
        path (str): The path to the file in which the content will be appended.
        content(str): The content to append to the file.

        Returns:
        bool: True if the content was successfully written, False otherwise.

        Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path to the file is a directory.
        PermissionError: If there is a lack of permission to access the file.
        OSError: For other I/O related errors.
        """
        try:
            with open(path, mode) as opened_file:
                opened_file.write(content)
                log.info("[F_HANDLER] Successfully added contents to file.")
                return True
        except FileNotFoundError:
            log.err(f"[F_HANDLER] File at path '{path}' not found.")
        except IsADirectoryError:
            log.err(f"[F_HANDLER] The specified path '{path}' is a directory.")
        except PermissionError:
            log.err(f"[F_HANDLER] You do not have permission to access the file.")
        except OSError as err:
            log.err(f"[F_HANDLER] An I/O error has occurred: {err}")
        
        return False
        
    def read_file(self, path: str) -> str:
        """
        Reads a file and returns the content.

        Parameters:
        path(str): Path to the file.

        Returns:
        file_contents(str): The contents of the file that was read.
        None: If there was an exception and the file was not read.

        Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path to the file is a directory.
        PermissionError: If there is a lack of permission to access the file.
        OSError: For other I/O related errors.
        """
        try:
            with self.open_file(path, "r") as opened_file:
                file_contents = opened_file.read()
                log.info("[F_HANDLER] Successfully read contents.")
                return file_contents
        except FileNotFoundError:
            log.err(f"[F_HANDLER] File at path '{path}' not found.")
        except IsADirectoryError:
            log.err(f"[F_HANDLER] The specified path '{path}' is a directory.")
        except PermissionError:
            log.err(f"[F_HANDLER] You do not have permission to access the file.")
        except OSError as err:
            log.err(f"[F_HANDLER] An I/O error has occurred: {err}")
        
        return ""
