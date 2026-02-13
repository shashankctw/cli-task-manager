CLI Task Manager

A command-line task manager built in Python to demonstrate clean,
structured, and pythonic code design.

This application supports task creation, completion, deletion, priority
management, and due dates using JSON-based persistence.

------------------------------------------------------------------------

FEATURES

-   Add new tasks
-   Assign priority (low, medium, high)
-   Add optional due dates (YYYY-MM-DD)
-   View tasks sorted by priority
-   Mark tasks as completed
-   Delete tasks
-   Persistent storage using JSON
-   Input validation for date and priority fields

------------------------------------------------------------------------

TECH STACK

-   Python 3
-   Standard Library (json, os, datetime)

No external dependencies.

------------------------------------------------------------------------

PROJECT STRUCTURE

cli-task-manager/ │ ├── main.py ├── tasks.json ├── .gitignore
└── README.md

------------------------------------------------------------------------

INSTALLATION

Clone the repository:

git clone https://github.com/shashankctw/cli-task-manager.git cd
cli-task-manager

Run the application:

main.py

------------------------------------------------------------------------

USAGE

After running the script, you will see an interactive menu:

Task Manager 1. Add Task 2. View Tasks 3. Mark Task as Complete 4.
Delete Task 5. Exit

Follow the prompts to manage tasks.

------------------------------------------------------------------------

DATA STRUCTURE

Tasks are stored in tasks.json using the following format:

{ “1”: { “title”: “Learn Python”, “status”: “pending”, “priority”:
“high”, “due_date”: “2026-03-01” } }

Each task contains: - title - status (pending or completed) - priority -
due_date

------------------------------------------------------------------------

CONCEPTS DEMONSTRATED

-   Structured procedural design
-   JSON file persistence
-   Input validation
-   Sorting by priority
-   Clean command-line interaction
-   Separation of concerns

------------------------------------------------------------------------

LICENSE

This project is licensed under the MIT License.
