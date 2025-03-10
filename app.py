from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
import json
import os
import csv

app = Flask(__name__)

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
    title = request.form.get("title")
    if title:
        new_task = {"id": len(tasks) + 1, "title": title, "status": "Новая"}
        tasks.append(new_task)
        save_tasks(tasks)
    return redirect(url_for("index"))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    """Edits a task with the specified ID."""
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = request.form.get("title", task["title"])
            task["status"] = request.form.get("status", task["status"])
            save_tasks(tasks)
            break
    return redirect(url_for("index"))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Deletes a task with the specified ID."""
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))

@app.route('/search', methods=['GET'])
def search():
    """Searches for tasks based on the provided query."""
    query = request.args.get("query", "").lower()
    filtered_tasks = [task for task in tasks if query in task["title"].lower()]
    return render_template("index.html", tasks=filtered_tasks)

@app.route('/filter', methods=['GET'])
def filter_tasks():
    """Filters tasks based on their status."""
    status = request.args.get("status")
    if status:
        filtered_tasks = [task for task in tasks if task["status"] == status]
    else:
        filtered_tasks = tasks
    return render_template("index.html", tasks=filtered_tasks)

@app.route('/export')
def export_tasks():
    """Exports tasks as a CSV file."""
    csv_filename = "tasks_export.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Status"])
        for task in tasks:
            writer.writerow([task["id"], task["title"], task["status"]])
    return send_file(csv_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
