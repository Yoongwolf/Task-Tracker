import sys
import json
import os
from datetime import datetime

# File Handler
FILE_PATH = "tasks.json"

def read_tasks():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def write_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=4)

# Task Manager
class TaskManager:
    def __init__(self):
        self.tasks = read_tasks()

    def _generate_id(self):
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1

    def add_task(self, description):
        task = {
            "id": self._generate_id(),
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat()
        }
        self.tasks.append(task)
        write_tasks(self.tasks)
        print(f"Task added successfully (ID: {task['id']})")

    def list_tasks(self, status=None):
        if status:
            filtered_tasks = [task for task in self.tasks if task["status"] == status]
        else:
            filtered_tasks = self.tasks

        if not filtered_tasks:
            print("No tasks found.")
            return

        for task in filtered_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, "
                  f"Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")

# CLI Parser
def main():
    task_manager = TaskManager()

    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: task-cli add <description>")
        else:
            description = " ".join(sys.argv[2:])
            task_manager.add_task(description)

    elif command == "list":
        if len(sys.argv) == 2:
            task_manager.list_tasks()
        elif sys.argv[2] in ["todo", "done", "in-progress"]:
            task_manager.list_tasks(sys.argv[2])
        else:
            print("Usage: task-cli list [todo|done|in-progress]")

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
