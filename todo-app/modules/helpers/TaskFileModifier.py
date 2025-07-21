from tools.FileHandler import FileHandler
from tools.logger import Logger

class TaskFileModifier:
    def __init__(self, task_path: str):
        self.task_path = task_path
        self.log = Logger("log/program.log")

    def save_result(self, task_path:str, task_list: list) -> bool:
        file_handler = FileHandler("ERASE_WRITE_FILE")
        result_to_write = ""

        for task in task_list:
            result_to_write += f"{task}\n"

        print(result_to_write)

        return file_handler.write_file(task_path, result_to_write)

    def locate_task(self, task_path: str, task_index_tracking: int) -> str:
        file_handler = FileHandler("READ_FILE")

        tasks_list = file_handler.read_file(task_path)

        if (tasks_list.strip() != ""):
            tasks_list = tasks_list.split("\n")

            if tasks_list[-1] == "" or tasks_list[-1] == " ":
                tasks_list.pop()

        for task in tasks_list:
            current_task_splitted = task.split(",")

            if int(current_task_splitted[0]) == task_index_tracking:
                self.log.info("[TASK_MODIFIER] Located tracked task.")
                return task
        
        return ""

    def delete_task(self, task_path: str, tracked_index: int) -> bool:
        file_handler = FileHandler("READ_FILE")

        tasks_list = file_handler.read_file(task_path)

        if (tasks_list.strip() != ""):
            tasks_list = tasks_list.split("\n")

            if tasks_list[-1] == "" or tasks_list[-1] == " ":
                tasks_list.pop()

            located_task = self.locate_task(task_path, tracked_index)
            tasks_list.remove(located_task) if located_task != "" else ""

            return self.save_result(task_path, tasks_list)
    
        return False
