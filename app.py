from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_id, task_name, completed = (
                    line.strip().split("|")
                )

                tasks.append({
                    "id": int(task_id),
                    "name": task_name,
                    "completed": completed == "True"
                })

    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(
    f"{task['id']}|{task['name']}|{task['completed']}\n"
)

load_tasks()

@app.route("/")
def home():
    return render_template(
        "index.html",
        tasks=tasks
        )

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]

    new_task = {
    "id": max([task["id"] for task in tasks], default=0) + 1,
    "name": task,
    "completed": False
}

    tasks.append(new_task)

    import os
    print("CURRENT DIRECTORY:", os.getcwd())

    save_tasks()
    
    print("Saved:", new_task)

    return redirect(url_for("home"))

@app.route("/delete", methods=["POST"])
def delete():
    task_id = int(request.form["task_id"])

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

    save_tasks()

    return redirect(url_for("home"))

@app.route("/edit", methods=["POST"])
def edit():
    task_id = int(request.form["task_id"])
    new_name = request.form["new_name"]

    for task in tasks:
        if task["id"] == task_id:
            task["name"] = new_name

    save_tasks()

    return redirect(url_for("home"))

@app.route("/complete", methods=["POST"])
def complete():
    task_id = int(request.form["task_id"])

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]

    save_tasks()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

