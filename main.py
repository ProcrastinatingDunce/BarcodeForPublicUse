print("Hello BarCode")

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
  if request.method == "GET":
    return "<h1> _id = 123 <br/> Name = Soap <br/> Price = 1200 </h1>"
  elif request.method == "POST":
    text = request.get_json()
    return text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
