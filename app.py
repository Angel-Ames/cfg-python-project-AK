
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def say_hello():
    return render_template("index.html")

# <> mean that you can input any text
@app.route("/<name>") 
def say_hello_to(name):
    return render_template("index.html", user=name)

@app.route("/About") 
def about_page():
    return render_template("About.html")

@app.route("/contact") 
def contact_page():
    return render_template("contact.html")

@app.route("/Phoebe") 
def Phoebe_page():
    return render_template("Phoebe.html")

@app.route("/Pancake") 
def Pancake_page():
    return render_template("Pancake.html")

@app.route("/<int:number1>/<int:number2>")
def show_two_numbers_total(number1, number2):
    total= number1 + number2
    return render_template("total.html", number1= number1, number2=number2, total=total)

@app.route("/feedback", methods=["POST"])
def get_feedback():
  # request.values is a dictionary holding any
  # POST request data that's not already part of the URL
  data = request.values

  return render_template("feedback.html", form_data=data)
  
if 'PORT' in os.environ:
     app.run(host='0.0.0.0', port=int(os.environ['PORT']))
else:
     app.run(debug=True)