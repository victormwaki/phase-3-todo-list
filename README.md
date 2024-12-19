# phase-3-todo-list

# Todo CLI App with SQLite

This project is a command-line interface (CLI) application for managing a to-do list using Python and SQLite. The app provides functionalities to add, update, delete, and complete tasks, while displaying them in a structured format using `rich` tables.

## Requirements

To run this application, make sure you have the following installed:

- Python 3.8 or higher
- Required Python packages:
  - `typer`
  - `rich`

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**
   bash
   pip install typer rich


## Usage Instructions

Run the app using the following command:
bash
python todocli.py

### Available Commands

- **Add a Todo**:
  bash
  python todocli.py add "task" "category"

  Example:
  bash
  python todocli.py add "Complete Python project" "Study"

- **Delete a Todo**:
  ```bash
  python todocli.py delete position
  ```
  Example:
  ```bash
  python todocli.py delete 1
  ```

- **Update a Todo**:
  ```bash
  python todocli.py update position --task "new_task" --category "new_category"
  ```
  Example:
  ```bash
  python todocli.py update 1 --task "Complete CLI app" --category "Programming"
  ```

- **Complete a Todo**:
  ```bash
  python todocli.py complete position
  ```
  Example:
  ```bash
  python todocli.py complete 1
  ```

- **Show All Todos**:
  ```bash
  python todocli.py show
  ```

---

## Example Workflow

1. **Add a Task**:
   ```bash
   python todocli.py add "Buy groceries" "Errands"
   python todocli.py add "Watch tutorial on SQLite" "Learning"
   ```

2. **View Tasks**:
   ```bash
   python todocli.py show
   ```
   Output:
   ```
   Todos! 💻
   ┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
   ┃ #   ┃ Todo                    ┃ Category     ┃ Done       ┃
   ┡━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
   │ 1   │ Buy groceries           │ [cyan]Errands[/cyan]     │ ❌          │
   │ 2   │ Watch tutorial on SQLite │ [green]Learning[/green]   │ ❌          │
   └─────┴─────────────────────────┴──────────────┴────────────┘
   ```

3. **Mark a Task as Complete**:
   ```bash
   python todocli.py complete 1
   ```

4. **Delete a Task**:
   ```bash
   python todocli.py delete 2
   ```

5. **Update a Task**:
   ```bash
   python todocli.py update 1 --task "Go grocery shopping" --category "Errands"
   ```

---

## Project Structure

```
project-folder/
├── database.py      # Handles database operations with SQLite
├── model.py         # Defines the Todo model
├── todocli.py       # Main CLI application
├── README.md        # Documentation for the project
```

