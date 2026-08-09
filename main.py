from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("result.html")


#TODO: finish this once and for all.










if __name__ == "__main__":
    main()
