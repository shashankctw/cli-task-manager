import os
import json
from datetime import datetime

# File to store tasks.
FILE_NAME = "tasks.json"
VALID_PRIORITIES = ["low", "medium", "high"]

# Load tasks from the file.
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
    return tasks

# Save tasks to the file.
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
            
# Add a new task.
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter task priority (low, medium, high): ").lower()
    while priority not in VALID_PRIORITIES:
        print("Invalid priority. Please enter low, medium, or high.")
        priority = input("Enter task priority (low, medium, high): ").lower()
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Task will be added without a due date.")
            due_date = None
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "priority": priority, "due_date": due_date, "status": "pending"}
    print(f"Task '{title}' added with ID {task_id}.")
    
# View all tasks.
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task_id, task in tasks.items():
        print(f"ID: {task_id}, Title: {task['title']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {task['status']}")
        
# Mark a task as completed.
def complete_task(tasks):
    task_id = int(input("Enter task ID to mark as completed: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "completed"
        print(f"Task ID {task_id} marked as completed.")
    else:
        print("Task ID not found.")
        
# Delete a task.
def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task ID {task_id} deleted.")
    else:
        print("Task ID not found.")
        
# Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()