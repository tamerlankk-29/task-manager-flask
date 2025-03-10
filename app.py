from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

# Create a Flask application instance
app = Flask(__name__)

# Define the filename for storing the task list
TASKS_FILE = "tasks.json"


def load_tasks():
    """Loads the task list from a file if it exists, otherwise returns an empty list."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Saves the task list to a file in JSON format."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


# Load tasks when the application starts
tasks = load_tasks()


@app.route('/')
def index():
    """Main page that displays the list of tasks."""
    return render_template("index.html", tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    """Adds a new task received from the form."""
    title = request.form.get("title")  # Get the task title from the form
    if title:
        new_task = {"id": len(tasks) + 1, "title": title, "status": "Новая"}  # Create a new task
        tasks.append(new_task)  # Add it to the list
        save_tasks(tasks)  # Save the updated task list
    return redirect(url_for("index"))  # Redirect to the main page


@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    """Edits a task with the specified ID."""
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = request.form.get("title", task["title"])  # Update the title if provided
            task["status"] = request.form.get("status", task["status"])  # Update the status if provided
            save_tasks(tasks)  # Save the changes
            break
    return redirect(url_for("index"))  # Redirect to the main page


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Deletes a task with the specified ID."""
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]  # Filter the task list, excluding the deleted task
    save_tasks(tasks)  # Save the updated list
    return redirect(url_for("index"))  # Redirect to the main page


@app.route('/search', methods=['GET'])
def search():
    """Searches for tasks based on the provided query."""
    query = request.args.get("query", "").lower()  # Get the search query and convert it to lowercase
    filtered_tasks = [task for task in tasks if query in task["title"].lower()]  # Filter tasks by title
    return render_template("index.html", tasks=filtered_tasks)  # Display the search results


if __name__ == '__main__':
    # Run the Flask server in debug mode
    app.run(debug=True)
