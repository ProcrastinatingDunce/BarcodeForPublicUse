import os
from flask import Flask, request
from mongo import DB

app = Flask(__name__)
db = DB(os.getenv("MONGO_CONN_STRING"))
db.get_database()

@app.route("/")
def index():
  return "Hello"

@app.route("barpost/{postid}/{price}", methods=["GET", "POST"])
def submit():
  if request.method == "GET":
      return db.get_items()
  elif request.method == "POST":
    text = request.get_json()
    db.insert_items(text)
    return 

@app.route("barget", methods=["GET"])
def barget():
    return 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
