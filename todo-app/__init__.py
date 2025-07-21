from modules.controller.TaskController import TaskController
from modules.controller.MenuController import MenuController
from modules.coordinators.AppCoordinator import AppCoordinator

def start():
    menu_instance = MenuController()
    task_controller = TaskController()
    app_coordinator = AppCoordinator(menu_instance, task_controller)

    while True:
        app_coordinator.runApplication()

if (__name__ == "__main__"):
    start()
