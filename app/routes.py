from flask import render_template, request, redirect, url_for
from app import app

posts = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        city = request.form.get("city")
        hobby = request.form.get("hobby")
        if all([name, age, city, hobby]):
            posts.append({"name": name, "age": age, "city": city, "hobby": hobby})
            return redirect(url_for("index"))
    return render_template("userdata.html", posts=posts)
