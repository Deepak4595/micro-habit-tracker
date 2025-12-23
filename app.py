from flask import Flask, render_template, redirect

app = Flask(__name__)

# Temporary in-memory habit list
habits = [
    {"name": "Drink Water", "done": False},
    {"name": "Read 10 Pages", "done": False},
    {"name": "Morning Walk", "done": False}
]

@app.route("/")
def index():
    completed = sum(1 for h in habits if h["done"])
    progress = int((completed / len(habits)) * 100)
    return render_template("index.html", habits=habits, progress=progress)

@app.route("/toggle/<int:id>")
def toggle(id):
    habits[id]["done"] = not habits[id]["done"]
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
