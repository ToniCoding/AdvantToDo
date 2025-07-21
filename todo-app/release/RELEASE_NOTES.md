# Changelog

All important notes about this project will be documented in this file.

*[11/03/2025] - The README file has been updated and reorganized for better readability. Added one table for easier version tracking.*

## [DISCLAIMER] This is unreleased software.
###### This software will be releasing one version a month.

*Note: By "something pending" we mean if some functionality or bug fixing that was initially planned for that version is done or not.*

| **Release version** | **Release date** | **New features** | **Bug fixing** | **Is something pending**
|---------------------|------------------|------------------|-----------------|-----------------|
| V_0.1.0| 23/02/2025| Yes| No| No|
| V_0.2.0| 16/06/2025| Yes| Yes| Yes|

## [0.1.0] - Release date - 23/02/2025

### Added
- Established the basic project structure.
- Created the "modules" directory and implemented the MVC pattern within it.
- Removed the dependency of importing both "Task" and "TaskController"; now only "TaskController" needs to be imported.

### Known Issues
- The due date format can be DD/MM/YY.
    - Possible approach: This can be addressed by enforcing the user to use YYYY or translating YY into YYYY format. This may be configured through `preferences.json`.
    - Tasks are currently being created in the year directory instead of the month directory.

## [0.2.0] - Release Date - 16/06/2025

### Added
- Registration of new tasks with name, description, and due date.
- Added `strTools` module containing utility methods such as `complyWithLen`.
- Implemented a task status system using an `enum` to represent various states: *Not Started*, *In Progress*, *Completed*, and *Blocked*.
- Created the `datetimeParser` module with tools for date validation and month translation.
- Enabled dynamic creation of required directories for task registration.
- Introduced dedicated logging functionality in `TaskController`.
- Added a main guard in the core file `main`.
- Added configuration file at `config/app_config.json` in JSON format.
- Added schema for the configuration file at `config/schemas/app_config-schema.json`.
- Implemented `software_info` module to manage software metadata, including social media links and version info.
- Introduced `AppCoordinator` to improve communication between controllers.
- Added an exit option and improved execution handling in `handle_task_center_action` within `AppCoordinator`.
- Created the `interfaces` directory to store menu-related interfaces.
- Developed `task_center_intf` to manage the task center interface and its functional calls.
- All interactions with the task center are now handled through `task_center_intf`.
- Added an option in `task_center_intf` to exit the software along with the task center.
- Implemented input validation through `check_if_integer` in `task_center_intf`.
- Created `Exceptions` directory in `modules/Exceptions`.
- Developed `modules/Exceptions/CustomExceptions` to store all custom exceptions used across the software.
- All files now include proper docstrings.
- Tasks are now displayed in a formatted table.
- Created `structureValidator` to handle logic for validating project structure.
- A screen cleanup is now executed when entering the task interface.
- The software now runs in a continuous loop; exiting requires selecting the exit option from the main menu (implemented in `main`).
- Successful task registration now logs and prints a confirmation message.
- Created `helpers` directory inside `modules` to store utilities following the MVC methodology.
- Developed `JSONReader` helper to load configuration and preferences files.
- Tasks are now assigned unique IDs.
- The `TaskView` table now displays an ID for each task.
- Added `remove_initial_spaces_from_string` utility method to `strTools`.
- Added more information fields to software information in `app_config`.
- Added `preferences-schema`.

### Changed
- Refactored `set_task_status` method to use `enum` values instead of boolean flags.
- Renamed the `app` directory to `controllers`.
- Renamed the `task_center_intf` file to `TaskCenterIntf` for naming consistency.
- Renamed `MenuVisuals` to `MenuView` along with its main class.
- Extracted data management responsibilities from `MenuController` into a new `MenuModel`.
- Updated `register_task` method to raise a custom `TaskDetailsException` when the provided input is invalid.
- Handled `TaskDetailsException` appropriately within `register_task`.
- Changed `showTask` method in `TaskView` to return a `list` instead of a `string`.
- Renamed `showTask` method to `getTasks`.
- Updated `Logger` to create the corresponding log file from its `__init__` constructor if it doesn't already exist.
- Improved exception messages for both handled and unhandled cases in `TaskController`.
- Setters in the `Task` class now raise `TaskDetailException` instead of returning status values.
- Task constraints are now loaded from the configuration file via `JSONReader` and enforced within the setters in `Task`.
- The software no longer returns to the main menu after each task action; it remains in the task center until explicitly exited.
- The software now executes a screen clear after each main menu action. This helps to keep user-shown data clear.
- Updated `app_config-schema`.
- Renamed directory `changelog` to `release`.

### Fixed
- Resolved a circular import issue between `FileHandler` and `Logger`.
- Fixed a bug where task descriptions were accepted without validating date format.
- Fixed an issue where the description was registered with two leading spaces.
- Resolved an issue where descriptions were saved without spaces between words.
- Fixed a bug where the first character or space in the description was being removed. This also caused single-character descriptions to be lost.
- Prevented task file overwrites by changing the file mode in `TaskController` from write to append.
- Corrected validation logic for task details in `Task`.
- Fixed a bug in `monthTranslator` where it returned the first two letters instead of the first three of a translated month.
- Handled the case where the absence of the current month’s task file caused an exception.

### Pending
- Structure verification: Ensures the integrity of the project to prevent software malfunctions.
- Task actions:
    - Edit tasks (modify fields individually).
    - Delete tasks.

### Known Issues
- *(No known issues listed at this time.)*

## [0.3.0] - Release Date - Unreleased
> *Project Foundation Update*

### Added
- **Implemented Git.**
- **Implemented Poetry.**
- **Implemented code health and linter tools.**


### Changed
- Deleted `operate_file` method as it was violating the single responsability principle.
- General code refactor to fix data typing consistency.
- *Started naming releases.*
