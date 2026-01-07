from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.htm")

@app.route("/hello")
def hello():
    name = request.args.get("name")
    return render_template("hello.html", namn=name)

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    return "Hej " + name

if __name__ == "__main__":
    app.run()