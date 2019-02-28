from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def say_hello():
    return render_template("index.html")

# <> mean that you can input any text
@app.route("/<name>") 
def say_hello_to(name):
    return render_template("bonus_index.html", user=name)

@app.route("/<int:number1>/<int:number2>")
def show_two_numbers_total(number1, number2):
    total= number1 + number2
    return render_template("total.html", number1= number1, number2=number2, total=total)

app.run(debug=True)