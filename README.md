# Task Manager (Python CLI Application)

## Overview

Task Manager is a command-line application built using Python that helps users create, manage, prioritize, and track their daily tasks.

The application allows users to add, view, update, and delete tasks through a simple menu-driven interface. Tasks are automatically saved to a local text file, ensuring that data remains available even after the application is closed. Users can also export their tasks to JSON format for backup and structured data storage.

This project demonstrates the implementation of core Python concepts including file handling, data persistence, JSON processing, dictionaries, and CRUD operations.



## Features

### Task Management

- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks

### Priority Management

- Assign task priorities:
  - High
  - Medium
  - Low

### Automatic Data Storage

- Tasks are automatically saved to `tasks.txt`
- Previously saved tasks are loaded when the application starts
- Data remains available between program executions

### JSON Export

- Export tasks to `tasks.json`
- Useful for backup and structured data storage

### User-Friendly Interface

- Simple menu-driven command-line application
- Easy navigation through numbered options



## Technologies Used

- Python 3
- File Handling
- JSON Module
- Dictionaries
- Nested Dictionaries
- Command Line Interface (CLI)



## Project Structure

```text
PROJECT-1_Task manager_Day7.py
tasks.txt
tasks.json
```

### File Description

- `PROJECT-1_Task manager_Day7.py` → Main application source code
- `tasks.txt` → Stores task data permanently
- `tasks.json` → JSON export file


## How to Run

### Clone the Repository

```bash
git clone https://github.com/Rishitbuilds/Rishit_builds.git
```

### Navigate to the Project Folder

```bash
cd Rishit_builds
```

### Run the Application

```bash
python PROJECT-1_Task manager_Day7.py
```


## Sample Menu

Task Manager Menu

1. Add task
2. View task
3. Mark task as completed
4. Delete task
5. Set Priority
6. Export to JSON
7. Exit


## Concepts Implemented

### Functions

- `add_tasks()`
- `view_tasks()`
- `mark_task_complete()`
- `delete_task()`
- `save_tasks()`
- `load_tasks()`

### Data Structures

- Dictionaries
- Nested Dictionaries

### CRUD Operations

- Create → Add Tasks
- Read → View Tasks
- Update → Mark Complete, Set Priority
- Delete → Remove Tasks

### Loops

- `for`
- `while`

### Conditional Statements

- `if`
- `elif`
- `else`

### File Handling

- Reading files
- Writing files
- Persistent data storage

### JSON Handling

- Exporting task data using the `json` module

### Data Persistence

- Saving tasks before exit
- Loading saved tasks when the application starts

### String Manipulation

- `split()`
- `strip()`
- `f-strings`

### Built-in Functions

- `max()`
- `enumerate()`
- `int()`
- `print()`

### Dictionary Methods

- `items()`
- `get()`
- `pop()`
- `update()`

### Python Modules

- `os`
- `json`



## Challenges Solved

### Automatic Task ID Generation

Implemented automatic task ID creation using:

```python
max(tasks.keys(), default=0) + 1
```

### Task Re-indexing After Deletion

When a task is deleted, the remaining tasks are automatically reassigned sequential IDs.

### Persistent Storage

Implemented file-based storage using `tasks.txt` so tasks remain available after restarting the application.

### JSON Export

Added functionality to export task data into JSON format.

### Priority Management

Implemented support for High, Medium, and Low priority tasks.



## Key Learnings

Through this project, I gained hands-on experience with:

- Building a menu-driven CLI application
- Implementing CRUD operations using Python
- Managing data using dictionaries and nested dictionaries
- Working with file handling for persistent storage
- Exporting application data using JSON
- Organizing code using functions and modular design
- Handling user input and application flow
- Managing and tracking tasks in a practical real-world scenario
- Maintaining data between program executions
- Designing solutions for task organization and productivity management



## Future Improvements

Potential enhancements include:

- Due dates and deadlines
- Task categories
- Search functionality
- Sorting and filtering tasks
- Colored terminal output
- GUI version using Tkinter
- SQLite database integration


## Author

Rishit

Python Developer | Building Projects and Learning by Practice
