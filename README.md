# Todo CLI Application

## Overview
This is a command-line Todo application built with Python. The app uses SQLAlchemy for database management, Typer for command-line interface handling, and Rich for displaying tables in the terminal.

## Features
- Add tasks with a category.
- View a list of all tasks.
- Update task details (name or category).
- Mark tasks as completed.
- Delete tasks.

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
- The database will be automatically initialized when the app runs for the first time. If you encounter errors related to the schema, delete the `todos.db` file to allow SQLAlchemy to recreate it.

## Usage

### Run the CLI App
```bash
python todocli.py --help
```
This will display the list of available commands:

```text
Usage: todocli.py [OPTIONS] COMMAND [ARGS]...

Commands:
  add       Adds a task with a category.
  complete  Marks a task as completed.
  delete    Deletes a task by its position.
  show      Displays all tasks.
  update    Updates a task's name or category.
```

### Examples

#### Add a Task
```bash
python todocli.py add "Learn SQLAlchemy" "Study"
```

#### Show All Tasks
```bash
python todocli.py show
```

#### Mark a Task as Completed
```bash
python todocli.py complete 1
```

#### Update a Task
```bash
python todocli.py update 1 --task "Master SQLAlchemy"
```

#### Delete a Task
```bash
python todocli.py delete 1
```

## File Structure
```
.
├── database.py       # Database setup and operations using SQLAlchemy.
├── model.py          # Defines the Todo model.
├── todocli.py        # CLI application logic.
├── requirements.txt  # Python dependencies.
├── todos.db          # SQLite database (generated automatically).
└── README.md         # This file.
```

## Troubleshooting

### OperationalError: no such column: todos.id
This error occurs if the database schema doesn't match the SQLAlchemy model. To fix this:
1. Delete the `todos.db` file:
   ```bash
   rm todos.db
   ```
2. Run the app again to recreate the database.

### ModuleNotFoundError: No module named 'database'
Ensure all files (`database.py`, `model.py`, `todocli.py`) are in the same directory. Run the script from the directory containing these files.
