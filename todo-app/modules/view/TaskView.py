"""
This module defines the class `TaskView` which provides methods to display and transform tasks into a table
with their respective format.

Dependencies:
- `Logger` from `tools.logger` to log information.
- `tabulate` to display formatted tables.

Class:
    TaskView: Class that provides methods to transform and display registered tasks.

Methods:
    __init__(self) -> None:
        Initializes the `TaskView` class.

    showTaskTable(self, contents: list) -> str:
        Displays task contents in a formatted table.

    transformTask(self, task_list: list) -> list:
        Transforms a task list split by commas.
"""

from tools.logger import Logger
from tabulate import tabulate

log = Logger("log/program.log")

class TaskView:
    """
    Class that provides methods to display and transform tasks.

    Methods:
        __init__(self) -> None:
            Initializes the class without arguments.

        showTaskTable(self, contents: list) -> str:
            Displays tasks in a tabular format.

        transformTask(self, task_list: list) -> list:
            Transforms tasks from a list of comma-separated strings.
    """
    
    def __init__(self):
        """
        Initializes the `TaskView` class. This constructor takes no parameters and performs no actions.
        """
        pass

    def showTaskTable(self, contents: list) -> str:
        """
        Displays the tasks in a formatted table.

        Parameters:
        contents (list): Task list. All registered tasks with values corresponding to "Name", "Description", "Due date", and "Status".

        Returns:
        str: The task table in text format, using the `tabulate` package.
        """
        
        headers = ["ID", "Name", "Description", "Due date", "Status"]
        col_counter = ["left"] * len(headers)
        return tabulate(contents, headers=headers, colalign=col_counter)

    def transformTask(self, task_list: list) -> list:
        """
        Transforms a list of tasks represented as comma-separated strings
        into a list of lists of strings.

        Parameters:
        task_list (list): List of tasks, where each task is a comma-separated string.

        Returns:
        list:
         List of lists where each sublist contains the elements of the comma-separated task.
        """

        transformed_tasks = []

        for task in task_list:
            splitted_task = task.split(',')
            transformed_tasks.append(splitted_task)

        return transformed_tasks
