from flask import Flask, render_template, request
from pymongo import MongoClient 


app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["user_database"]
users_c = db["responses"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def sub():
    form_doc = {
    "first_name": request.form.get("t1"),
     "last_name": request.form.get("t2"),
     "gender" : request.form.get("gnd"),
     "email": request.form.get("t3"),
     "date_of_birth": request.form.get("dt"),
     "phone_number" : request.form.get("t4"),
     "id":request.form.get("t5"),
     "career":request.form.get("sel")
}

    record = users_c.insert_one(form_doc)

    return render_template("result.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
