#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter

@app.route("/count/<int:parameter>")
def count(parameter):
    counter = ""
    for i in range(0, parameter):
        counter = counter + f"{i}\n"
    return counter

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):

    if operation == "div":
        answer = int(num1) / int(num2)
    elif operation == "+":
        answer = int(num1) + int(num2)
    elif operation == "-":
        answer = int(num1) - int(num2)
    elif operation == "*":
        answer = int(num1) * int(num2)
    elif operation == "%":
        answer = int(num1) % int(num2)
    
    return str(answer)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
