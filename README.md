# Todo CLI App with SQLite

This project is a simple command-line interface (CLI) application for managing a to-do list using Python and SQLite. The app allows you to add, update, delete, complete, and display tasks.

---

## Requirements

- Python 3.8 or higher
- Required Python packages:
  - `typer`
  - `rich`

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install typer rich
   ```

---

## Usage

Run the app using:
```bash
python todocli.py
```

### Commands

- **Add a Task**:
  ```bash
  python todocli.py add "task" "category"
  ```
  Example:
  ```bash
  python todocli.py add "Complete Python project" "Study"
  ```

- **Delete a Task**:
  ```bash
  python todocli.py delete position
  ```
  Example:
  ```bash
  python todocli.py delete 1
  ```

- **Update a Task**:
  ```bash
  python todocli.py update position --task "new_task" --category "new_category"
  ```
  Example:
  ```bash
  python todocli.py update 1 --task "Complete CLI app" --category "Programming"
  ```

- **Mark a Task as Complete**:
  ```bash
  python todocli.py complete position
  ```
  Example:
  ```bash
  python todocli.py complete 1
  ```

- **Show All Tasks**:
  ```bash
  python todocli.py show
  ```

---

## Example

1. Add tasks:
   ```bash
   python todocli.py add "Buy groceries" "Errands"
   python todocli.py add "Watch tutorial on SQLite" "Learning"
   ```

2. View tasks:
   ```bash
   python todocli.py show
   ```

3. Mark a task as complete:
   ```bash
   python todocli.py complete 1
   ```

4. Delete a task:
   ```bash
   python todocli.py delete 2
   ```

5. Update a task:
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

