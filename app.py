from flask import Flask, render_template

app = Flask(__name__)

tasks = [
    "Workout",
    "Study Python",
    "Read Bible",
    "Run"
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        tasks=tasks
        )

if __name__ == "__main__":
    app.run(debug=True)

