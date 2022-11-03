print("Hello BarCode")

from flask import Flask, render_template, request

app = Flask("app")

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
  if request.method == "GET": # if form method is GET
    text = request.args["text"]
    return text
  elif request.method == "POST": # if form method is POST
    text = request.form["text"]
    return text

app.run(host="0.0.0.0", port=8080)
