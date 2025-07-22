"""
This module defines the class `TaskController` which provides methods to view and register tasks.

Dependencies:
- `FileHandler` from `tools.FileHandler` for file operations.
- `monthTranslator`, `getDateDetails` from `tools.datetimeParser` for date handling.
- `Task` from `modules.model.Task` for task management.
- `TaskView` from `modules.view.TaskView` for task visualization.
- `TaskDetailException` from `modules.exceptions.CustomExceptions` for custom exception handling.
- `makedirs` from `os` for directory creation.

Class:
    TaskController: Class that provides methods to view and register tasks.

Methods:
    __init__(self) -> None:
        Initializes the `TaskController` class.

    view_task(self) -> None:
        Displays tasks from a file in a tabular format.

    register_task(self) -> bool:
        Registers a new task and writes it to a file.
"""

from tools.FileHandler import FileHandler
from tools.datetimeParser import monthTranslator, getDateDetails
from tools.createAndVerifyDirsAndFile import createFullPathWithFile
from modules.model.Task import Task
from modules.view.TaskView import TaskView
from modules.helpers.TaskFileModifier import TaskFileModifier
from modules.exceptions.CustomExceptions import TaskDetailException

date_details = getDateDetails("ym")
form_path = f"tasks/{date_details[0]}/{monthTranslator((date_details[1]) - 1)}/tasks.txt"

file_handler = FileHandler("WRITE")
task_view = TaskView()
task_modifier = TaskFileModifier(form_path)

class TaskController:
    """
    Class that provides methods to view and register tasks.

    Methods:
        __init__(self) -> None:
            Initializes the class without arguments.

        view_task(self) -> None:
            Displays tasks from a file in a tabular format.

        register_task(self) -> bool:
            Registers a new task and writes it to a file.
    """
    
    def __init__(self) -> None:
        """
        Initializes the `TaskController` class. This constructor takes no parameters and performs no actions.
        """
        pass
    
    def view_task(self) -> None:
        """
        Displays tasks from a file in a tabular format.

        Retrieves the current year and month, constructs the file path, and reads tasks from the file.
        Transforms and displays the tasks in a table format using `TaskView`.

        Exceptions:
        Prints any exception that occurs during file reading or task processing.
        """
        date_details = getDateDetails("ym")
        form_path = f"tasks/{date_details[0]}/{monthTranslator((date_details[1]) - 1)}/tasks.txt"

        with open(form_path, "r") as task_file:
            task_content = []

            for line in task_file:
                line = line.strip()

                if line:
                    task_content.append(line)

            task_content = "\n".join(task_content).split("\n")

        task_table = task_view.showTaskTable(task_view.transformTask(task_content))

        print(task_table)

    def register_task(self) -> bool:
        """
        Registers a new task and writes it to a file.

        Prompts the user for task details, registers the task, and writes it to a file.
        Creates necessary directories if they do not exist.

        Returns:
        bool: True if the task was successfully written to the file, False otherwise.

        Exceptions:
        Handles `TaskDetailException` for task detail errors and prints any other exceptions.
        """
        task = Task()
        task_details = input("Details of your new task (name, description, date)\n- ").split(",")

        try:
            date_details = getDateDetails("ym")
            form_path = f"tasks/{date_details[0]}/{monthTranslator((date_details[1]) - 1)}"
            
            if not createFullPathWithFile(form_path, "tasks.txt"):
                return False

            form_path += "/tasks.txt"
            task.register_details(task_details, form_path)
            task_content = f"{task.get_task_details(form_path)}\n"

            with open(form_path, "a") as task_file:
                pass
        
            return True if file_handler.write_file(form_path, task_content, "a") else False
        
        except TaskDetailException as TDE:
            print(TDE)
            return False
        
        except TypeError as TyErr:
            print(TyErr)
            return False

        except FileNotFoundError as FNF:
            print(FNF)
            return False

        except Exception as e:
            print(f"An unhandled exception occurred: {e}")
            return False
        
    def delete_task(self, tracking_index: int) -> bool:
        date_details = getDateDetails("ym")
        form_path = f"tasks/{date_details[0]}/{monthTranslator((date_details[1]) - 1)}"
        form_path += "/tasks.txt"

        if (task_modifier.delete_task(form_path, tracking_index)):
            return True
        
        return False
    
    def edit_task(self, tracking_index: int) -> bool:
        date_details = getDateDetails("ym")
        form_path = f"tasks/{date_details[0]}/{monthTranslator((date_details[1]) - 1)}"
        form_path += "/tasks.txt"

        field_to_modify = int(input("Field to modify: "))

        if (task_modifier.edit_task(form_path, tracking_index, field_to_modify)):
            return True
        
        return False
