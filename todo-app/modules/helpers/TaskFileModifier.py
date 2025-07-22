from tools.FileHandler import FileHandler
from tools.logger import Logger

class TaskFileModifier:
    def __init__(self, task_path: str):
        self.task_path = task_path
        self.log = Logger("log/program.log")

    def locate_task(self, task_path: str, current_task_index_tracking: int) -> str:
        file_handler = FileHandler("READ")

        all_tasks_content = file_handler.read_file(task_path)

        if (all_tasks_content.strip() != ""):
            all_tasks_content = all_tasks_content.split("\n")

            if all_tasks_content[-1] == "" or all_tasks_content[-1] == " ":
                all_tasks_content.pop()

        for task in all_tasks_content:
            current_task_splitted = task.split(",")

            if int(current_task_splitted[0]) == current_task_index_tracking:
                self.log.info("[TASK_MODIFIER] Located tracked task.")
                return task
        
        return ""
    
    def save_updated_tasks_content(self, task_path:str, task_list: list) -> bool:
        file_handler = FileHandler("OVERWRITE")
        updated_tasks_content_to_write = ""

        for task in task_list:
            updated_tasks_content_to_write += f"{task}\n"

        return file_handler.overwrite_file(task_path, updated_tasks_content_to_write)

    def edit_task(self, task_path:str, tracked_index: int, edit_field: int) -> bool:
        file_handler = FileHandler("READ")
        all_tasks_content = file_handler.read_file(task_path)
        task_fields = ["name", "description", "due date"]

        if (all_tasks_content.strip() != ""):
            all_tasks_content = all_tasks_content.split("\n")

            if all_tasks_content[-1] == "" or all_tasks_content[-1] == " ":
                all_tasks_content.pop()

            task_to_edit = self.locate_task(task_path, tracked_index).split(",")
            task_to_edit_index = task_to_edit[0]

            match edit_field:
                case 1:
                    task_to_edit[edit_field] = input(f"New value for {task_fields[edit_field - 1]}: ")
                case 2:
                    task_to_edit[edit_field] = input(f"New value for {task_fields[edit_field - 1]}: ")
                case 3:
                    task_to_edit[edit_field] = input(f"New value for {task_fields[edit_field - 1]}: ")
                case 4:
                    task_to_edit[edit_field] = input(f"New value for {task_fields[edit_field - 1]}: ")
                case _:
                    raise IndexError("Out of bounds exception")
                    
            updated_tasks_content = ""
            processed_current_task_indexes = []

            for task in all_tasks_content:
                current_task_fields = task.split(",")
                current_task_index = current_task_fields[0]
                
                if current_task_index not in processed_current_task_indexes:
                    if current_task_index != task_to_edit_index and current_task_index < task_to_edit_index:
                        updated_tasks_content += str(current_task_fields)
                        processed_current_task_indexes.append(current_task_index)

                    if current_task_index == task_to_edit_index:
                        updated_tasks_content += str(task_to_edit)
                        processed_current_task_indexes.append(current_task_index)

                    if current_task_index != task_to_edit_index and current_task_index > task_to_edit_index:
                        updated_tasks_content += str(current_task_fields)
                        processed_current_task_indexes.append(current_task_index)

            
            updated_tasks_content = updated_tasks_content.strip().replace("[", "").replace("]", "\n").replace("'", "")

            if (file_handler.overwrite_file(task_path, updated_tasks_content)):
                return True
            
        return False


    def delete_task(self, task_path: str, tracked_index: int) -> bool:
        file_handler = FileHandler("READ")
        all_tasks_content = file_handler.read_file(task_path)

        if (all_tasks_content.strip() != ""):
            all_tasks_content = all_tasks_content.split("\n")

            if all_tasks_content[-1] == "" or all_tasks_content[-1] == " ":
                all_tasks_content.pop()

            task_to_edit = self.locate_task(task_path, tracked_index)
            all_tasks_content.remove(task_to_edit) if task_to_edit != "" else ""

            return self.save_updated_tasks_content(task_path, all_tasks_content)
    
        return False
