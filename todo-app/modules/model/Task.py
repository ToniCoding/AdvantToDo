"""
This module defines the class `Task` which provides methods to manage task details.

Dependencies:
- `complyWithLen`, `replace_special_chars_with_underscore` from `tools.strTools` for string manipulation.
- `isDateFormattedCorrectly` from `tools.datetimeParser` for date validation.
- `Logger` from `tools.logger` for logging.
- `TaskDetailException` from `modules.exceptions.CustomExceptions` for custom exception handling.
- `Enum` from `enum` for task status enumeration.

Class:
    Task: Class that provides methods to manage task details.

Methods:
    __init__(self, task_name: str = "None", task_description: str = "None", task_due: str = "None", task_status: bool = False) -> None:
        Initializes the `Task` class with optional task details.

    get_task_name(self) -> str:
        Returns the task name.

    set_task_name(self, new_task_name: str) -> bool:
        Sets the task name if it complies with length constraints.

    get_task_description(self) -> str:
        Returns the task description.

    set_task_description(self, new_task_description: str) -> bool:
        Sets the task description if it complies with length constraints.

    get_task_due(self) -> str:
        Returns the task due date.

    set_task_due(self, new_task_due: str) -> None:
        Sets the task due date if it is correctly formatted.

    get_task_status(self) -> str:
        Returns the task status.

    set_task_status(self, new_task_status: TaskStatus) -> None:
        Sets the task status if it is a valid `TaskStatus` enum.

    get_task_details(self) -> str:
        Returns a string with all task details.

    register_details(self, details: list) -> bool:
        Registers task details from a list.
"""

from tools.strTools import complyWithLen, replace_special_chars_with_underscore, remove_initial_spaces_from_string
from tools.datetimeParser import isDateFormattedCorrectly
from tools.fileExaminationTools import determine_file_size
from tools.logger import Logger
from modules.helpers.JSONReader import JSONReader
from modules.exceptions.CustomExceptions import TaskDetailException
from enum import Enum

log = Logger("log/program.log")
json_config = JSONReader("config/app_config.json")

class Task:
    """
    Class that provides methods to manage task details.

    Methods:
        __init__(self, task_name: str = "None", task_description: str = "None", task_due: str = "None", task_status: bool = False) -> None:
            Initializes the class with optional task details.

        get_task_name(self) -> str:
            Returns the task name.

        set_task_name(self, new_task_name: str) -> bool:
            Sets the task name if it complies with length constraints.

        get_task_description(self) -> str:
            Returns the task description.

        set_task_description(self, new_task_description: str) -> bool:
            Sets the task description if it complies with length constraints.

        get_task_due(self) -> str:
            Returns the task due date.

        set_task_due(self, new_task_due: str) -> None:
            Sets the task due date if it is correctly formatted.

        get_task_status(self) -> str:
            Returns the task status.

        set_task_status(self, new_task_status: TaskStatus) -> None:
            Sets the task status if it is a valid `TaskStatus` enum.

        get_task_details(self) -> str:
            Returns a string with all task details.

        register_details(self, details: list) -> bool:
            Registers task details from a list.
    """
    
    class TaskStatus(Enum):
        NOT_STARTED = 1
        IN_PROGRESS = 2
        FINISHED = 3
        BLOCKED = 4

    def __init__(self, task_name: str = "None", task_description: str = "None", task_due: str = "None", task_status: str = "PENDING") -> None:
        """
        Initializes the `Task` class with optional task details.

        Parameters:
        task_name (str): The name of the task. Default is "None".
        task_description (str): The description of the task. Default is "None".
        task_due (str): The due date of the task. Default is "None".
        task_status (bool): The status of the task. Default is False.
        """
        self.task_name = task_name
        self.task_description = task_description
        self.task_due = task_due
        self.task_status = task_status

        self.task_restrictions = json_config.get_task_configuration()

    def get_current_task_indexing(self, task_file_contents: str) -> int:
        """
        Reads a task file and returns the index of the last non-empty task line.

        The file should contain comma-separated lines. The function skips empty lines 
        (e.g., a trailing newline at the end of the file) and returns the first field 
        of the last valid line, converted to an integer.

        Args:
            task_file_contents (str): Path to the file containing the tasks.

        Returns:
            int: The integer value of the first field in the last non-empty line.
        """
        
        with open(task_file_contents, "r") as file:
            current_line = ""

            if determine_file_size(task_file_contents) == 0:
                return 1
            
            for line in file:
                if line.strip():
                    current_line = line.strip().split(",")

        return int(current_line[0]) + 1
    
    def set_task_current_index(self, current_index: int):
        self.task_index = current_index

    def get_task_name(self) -> str:
        """
        Returns the task name.

        Returns:
        str: The name of the task.
        """
        return self.task_name
    
    def set_task_name(self, new_task_name: str) -> None:
        """
        Sets the task name if it complies with length constraints.

        Parameters:
        new_task_name (str): The new name for the task.

        Raises:
        TaskDetailException: If the task name is longer than permitted.
        """
        if not complyWithLen(new_task_name, self.task_restrictions[0]):
            log.err("[TASK] Task name cannot be longer than 30 characters.")
            raise TaskDetailException("Task name cannot be longer than 30 characters.")
        
        log.info("[TASK] Correctly applied task name.")
        self.task_name = new_task_name

    def get_task_description(self) -> str:
        """
        Returns the task description.

        Returns:
        str: The description of the task.
        """
        return self.task_description

    def set_task_description(self, new_task_description: str) -> None:
        """
        Sets the task description if it complies with length constraints.

        Parameters:
        new_task_description (str): The new description for the task.

        Raises:
        TaskDetailException: If the task description is longer than permitted.
        """
        if not complyWithLen(new_task_description, self.task_restrictions[1]):
            log.err("[TASK] Task description cannot be longer than 500 characters.")
            raise TaskDetailException("Task description cannot be longer than 30 characters.")
        
        log.info("[TASK] Correctly applied task description.")

        self.task_description = remove_initial_spaces_from_string(new_task_description)
    
    def get_task_due(self) -> str:
        """
        Returns the task due date.

        Returns:
        str: The due date of the task.
        """
        return self.task_due
    
    def set_task_due(self, new_task_due: str) -> None:
        """
        Sets the task due date if it is correctly formatted.

        Parameters:
        new_task_due (str): The new due date for the task.

        Raises:
        TypeError: If the date format is incorrect.
        """
        new_task_due = replace_special_chars_with_underscore(new_task_due.replace(" ", ""))
        
        if isDateFormattedCorrectly(new_task_due):
            log.info("[TASK] Applied date to task due.")
            self.task_due = new_task_due
        else:
            log.err("[TASK] Date format is incorrect, it must follow the DD/MM/YYYY format.")
            raise TypeError("Date format is incorrect.")

    def get_task_status(self) -> str:
        """
        Returns the task status.

        Returns:
        str: The status of the task.
        """
        return self.task_status
    
    def set_task_status(self, new_task_status: TaskStatus) -> None:
        """
        Sets the task status if it is a valid `TaskStatus` enum.

        Parameters:
        new_task_status (TaskStatus): The new status for the task.

        Raises:
        ValueError: If `new_task_status` is not an instance of `TaskStatus`.
        """
        if not isinstance(new_task_status, self.TaskStatus):
            log.err("[TASK] An error occurred while setting the task status.")
            raise ValueError("new_task_status must be an instance of TaskStatus Enum")
        
        log.info(f"[TASK] Applied task status {new_task_status.name}.")
        self.task_status = new_task_status.name
    
    def get_task_details(self, task_file_path: str) -> str:
        """
        Returns a string with all task details.

        Returns:
        str: A comma-separated string of task details.
        """
        task_details = f"{self.get_current_task_indexing(task_file_path)},{self.get_task_name()},{self.get_task_description()},{self.get_task_due()},{self.get_task_status()}"
        return task_details

    def register_details(self, details: list, task_file_path: str) -> bool:
        """
        Registers task details from a list.

        Parameters:
        details (list): A list containing task details.
        task_file_path (string): The path to the corresponding task file.

        Returns:
        bool: True if the task details were registered successfully.

        Raises:
        TaskDetailException: If the number of details is incorrect.
        ValueError: If the index of details is out of bounds.
        """
        if len(details) < 3:
            log.err("[TASK] The amount of details specified is less than required.")
            raise TaskDetailException("The amount of details provided is less than required.")
        elif len(details) > 3:
            log.err("[TASK] The amount of details specified is more than required.")
            raise TaskDetailException("The amount of details provided is more than required.")
    
        self.set_task_current_index(self.get_current_task_indexing(f"{task_file_path}"))

        for i, detail in enumerate(details):
            match i:
                case 0:
                    self.set_task_name(detail)
                case 1:
                    self.set_task_description(detail)
                case 2:
                    self.set_task_due(detail)
                case _:
                    log.err("[TASK] The index of task details is out of bounds.")
                    raise ValueError("Index of details is out of bounds.")
            
        self.set_task_status(self.TaskStatus.NOT_STARTED)
        return True
