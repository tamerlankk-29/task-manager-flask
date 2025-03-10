# Task Manager

This project is a simple task manager built with Flask. It allows users to add, edit, delete, and search for tasks.

## 📌 Features
- Add tasks
- Edit tasks (change status)
- Delete tasks
- Search tasks by title

## 🛠️ Installation and Setup

### 1. Clone the Repository
```bash
    git clone https://github.com/your-repository/task-manager.git
    cd task-manager
```

### 2. Install Dependencies
```bash
    pip install flask
```

### 3. Run the Application
```bash
    python app.py
```
The application will start at `http://127.0.0.1:5000/`

## 📂 Project Structure
```
/task-manager
│── app.py                # Main Flask application code
│── tasks.json            # File for storing tasks
│── templates/
│   └── index.html        # HTML template for the main page
└── README.md             # This file
```

## 📜 Code Description

### app.py (Main Flask Server)
- `load_tasks()` – Loads tasks from `tasks.json`
- `save_tasks(tasks)` – Saves tasks to `tasks.json`
- `index()` – Displays the task list on the main page
- `add_task()` – Adds a new task
- `edit_task(task_id)` – Updates the task status
- `delete_task(task_id)` – Deletes a task
- `search()` – Searches for tasks by title

### index.html (User Interface)
- Task search form
- Task list with editing and deletion options
- Form for adding new tasks

## 📌 API Routes

| Method  | URL                 | Description |
|---------|---------------------|-------------|
| `GET`   | `/`                 | Main page with task list |
| `POST`  | `/add`              | Add a new task |
| `POST`  | `/edit/<task_id>`   | Edit a task |
| `GET`   | `/delete/<task_id>` | Delete a task |
| `GET`   | `/search?query=...` | Search for tasks |

## 🚀 Future Improvements
- Add the ability to edit task titles
- Implement user authentication
- Improve design using Bootstrap


