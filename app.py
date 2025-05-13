from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from database import get_db, init_db

app = Flask(__name__)
init_db()

@app.route("/")
def dashboard():
    conn = get_db()
    c = conn.cursor()
    tasks = c.execute("SELECT * FROM tasks ORDER BY created_at DESC").fetchall()
    health = c.execute("SELECT * FROM health ORDER BY date DESC LIMIT 1").fetchone()
    mood = c.execute("SELECT * FROM mood ORDER BY date DESC LIMIT 1").fetchone()
    gratitude = c.execute("SELECT * FROM gratitude ORDER BY date DESC LIMIT 1").fetchone()
    conn.close()
    return render_template("dashboard.html", tasks=tasks, health=health, mood=mood, gratitude=gratitude)

@app.route("/todo", methods=["GET", "POST"])
def todo():
    conn = get_db()
    c = conn.cursor()
    if request.method == "POST":
        content = request.form["content"]
        c.execute("INSERT INTO tasks (content) VALUES (?)", (content,))
        conn.commit()
        return redirect(url_for("todo"))
    tasks = c.execute("SELECT * FROM tasks ORDER BY created_at DESC").fetchall()
    conn.close()
    return render_template("todo.html", tasks=tasks)

@app.route("/delete-task/<int:id>")
def delete_task(id):
    conn = get_db()
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("todo"))

@app.route("/health") 
def health():
    return render_template("health.html")

@app.route("/mood") 
def mood():
    return render_template("mood.html")

@app.route("/gratitude") 
def gratitude():
    return render_template("gratitude.html")






# Driver code
if __name__ == "__main__":
    app.run(debug=True)
