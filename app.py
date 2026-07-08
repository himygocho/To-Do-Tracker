from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    
]

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
        "id": len(tasks) + 1,
        "name": task
    }

    tasks.append(new_task)
    return redirect(url_for("home"))

@app.route("/delete", methods=["POST"])
def delete():
    task_id = int(request.form["task_id"])

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

