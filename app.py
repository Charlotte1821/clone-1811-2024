from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    name = request.form.get("q")
    return render_template("main.html")

@app.route("/question1", methods=["GET"])
def question1():
    return render_template("question1.html")

@app.route("/question2", methods=["GET"])
def question2():
    return render_template("question2.html")

@app.route("/question3", methods=["GET"])
def question3():
    return render_template("question3.html")

@app.route("/question4", methods=["GET"])
def question4():
    return render_template("question4.html")

@app.route("/question5", methods=["GET"])
def question5():
    return render_template("question5.html")

if __name__ == "__main__":
    app.run(debug=True)



