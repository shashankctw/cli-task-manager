import os

# File to store tasks.
FILE_NAME = "tasks.txt"

# Load tasks from the file.
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split("|")
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks

# Save tasks to the file.
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id}|{task['title']}|{task['status']}\n")
            
# Add a new task.
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "pending"}
    print(f"Task '{title}' added with ID {task_id}.")
    
# View all tasks.
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task_id, task in tasks.items():
        print(f"ID: {task_id}, Title: {task['title']}, Status: {task['status']}")
        
# Mark a task as completed.
def complete_task(tasks):
    task_id = int(input("Enter task ID to mark as completed: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "completed"
        print(f"Task ID {task_id} marked as completed.")
    else:
        print("Task ID not found.")