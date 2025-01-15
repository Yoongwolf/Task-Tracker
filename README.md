# Task CLI

Task CLI is a simple command-line interface (CLI) application for managing tasks. It allows you to add, update, delete, and manage tasks stored in a JSON file. The application is lightweight, does not rely on external libraries, and is perfect for practicing file I/O and CLI interactions in Python.

## Features
- Add tasks with a description.
- Update task descriptions.
- Delete tasks by ID.
- Mark tasks as `in-progress` or `done`.
- List all tasks or filter tasks by status (`todo`, `in-progress`, `done`).
- Automatically creates a JSON file to store tasks if it doesn't exist.

## Project Page
You can find the project page at: [Task Tracker](https://roadmap.sh/projects/task-tracker)

## Requirements
- Python 3.x
- No external libraries are required.

## Getting Started

### Clone the Repository
```bash
git clone <repository-url>
cd task-cli
```

### Run the Application
Execute the script using Python:
```bash
python task_cli.py <command> [arguments]
```

## Commands

### Add a New Task
Adds a new task with the given description.
```bash
python task_cli.py add "<description>"
```
**Example:**
```bash
python task_cli.py add "Buy groceries"
```
**Output:**
```
Task added successfully (ID: 1)
```

### List Tasks
Lists all tasks or tasks filtered by status.
```bash
python task_cli.py list [status]
```
**Options for status:**
- `todo`: Lists all tasks with the status `todo`.
- `in-progress`: Lists tasks marked as `in-progress`.
- `done`: Lists tasks marked as `done`.

**Examples:**
```bash
python task_cli.py list
python task_cli.py list todo
```

### Update a Task
Updates the description of a task by ID.
```bash
python task_cli.py update <id> "<new description>"
```
**Example:**
```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a Task
Deletes a task by ID.
```bash
python task_cli.py delete <id>
```
**Example:**
```bash
python task_cli.py delete 1
```

### Mark a Task as In-Progress
Marks a task as `in-progress` by ID.
```bash
python task_cli.py mark-in-progress <id>
```
**Example:**
```bash
python task_cli.py mark-in-progress 2
```

### Mark a Task as Done
Marks a task as `done` by ID.
```bash
python task_cli.py mark-done <id>
```
**Example:**
```bash
python task_cli.py mark-done 2
```

## Task Properties
Each task is stored in the JSON file with the following properties:
- **id**: A unique identifier for the task.
- **description**: A short description of the task.
- **status**: The current status of the task (`todo`, `in-progress`, `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

## JSON File Structure
The tasks are stored in a file named `tasks.json` in the same directory as the script. Example structure:
```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": "2025-01-14T10:00:00",
        "updatedAt": "2025-01-14T10:00:00"
    }
]
```

## Error Handling
- **Invalid Command**: Displays a usage message if the command or arguments are incorrect.
- **Missing Task ID**: Displays an error if the specified task ID does not exist.
- **JSON File Issues**: Automatically creates an empty `tasks.json` file if it does not exist.

## Contributing
Contributions are welcome! If you'd like to add new features or improve the project, feel free to submit a pull request.

## License
This project is licensed under the MIT License.

---

Happy task managing! 🚀

