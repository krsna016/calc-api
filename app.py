# Using form:
# from flask import Flask,render_template,request,jsonify
# import math
# app = Flask(__name__)
# @app.route("/",methods = ['GET','POST'])
# def HomePage():
#     return render_template("index.html")
# @app.route("/math",methods = ["POST"])
# def math_operation():
#     if request.method=='POST':
#         oprs = request.form['operation']
#         num1 = int(request.form['num1'])
#         num2 = int(request.form['num2'])
#         if oprs == 'add':
#             result = f"The addition of {num1} and {num2} is : {num1 + num2}"
#             return render_template("results.html",result = result)
#         elif oprs == 'subtract':
#             result = f"The subtraction of {num1} and {num2} is : {num1 - num2}"
#             return render_template("results.html",result = result)
#         elif oprs == 'multiply':
#             result = f"The multiplication of {num1} and {num2} is : {num1 * num2}"
#             return render_template("results.html",result = result)
#         elif oprs == 'divide':
#             result = f"The division of {num1} and {num2} is : {num1 / num2}"
#             return render_template("results.html",result = result)
#         elif oprs == 'log':
#             result = f"The log of {num1} and {num2} is : {math.log(num1,num2)}"
#             return render_template("results.html",result = result)
# if __name__ == "__main__":
#     app.run(host="0.0.0.0")


# Using Postman
from flask import Flask,render_template,request,jsonify
import math
app = Flask(__name__)
@app.route("/",methods = ['GET','POST'])
def HomePage():
    return render_template("index.html")
@app.route("/postman_data",methods = ["POST"])
def math_operation_1():
    if request.method=='POST':
        oprs = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if oprs == 'add':
            result = f"The addition of {num1} and {num2} is : {num1 + num2}"
        elif oprs == 'subtract':
            result = f"The subtraction of {num1} and {num2} is : {num1 - num2}"
        elif oprs == 'multiply':
            result = f"The multiplication of {num1} and {num2} is : {num1 * num2}"
        elif oprs == 'divide':
            result = f"The division of {num1} and {num2} is : {num1 / num2}"
        elif oprs == 'log':
            result = f"The log of {num1} and {num2} is : {math.log(num1,num2)}"
        return jsonify(result)
if __name__ == "__main__":
    app.run(host="0.0.0.0")


