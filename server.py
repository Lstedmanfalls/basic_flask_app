from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route("/")
def index():
    session["counter"] = 0
    return render_template("index.html")

@app.route("/users", methods=["POST"])
def create_user():
    session["name"] = request.form["name"]
    session["email"] = request.form["email"]
    return redirect("/show")

@app.route("/show")
def show():
    return render_template('user.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pic.html'), 404

@app.route("/counter", methods=["POST"])
def counter():
    session["counter"] += 1
    return render_template("index.html")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

app.run(debug=True)
