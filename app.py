from flask import Flask, render_template , request , jsonify
import math

app = Flask(__name__)

# To render html page on web-browser
@app.route('/',methods = ['GET','POST'])
def home_page():
    return render_template('index.html')

# Below function must be called on click of Calculate button

@app.route('/math',methods = ['POST'])  #create route as defined in html
def math_operation():
    if(request.method == 'POST'): #If sending through form
        ops= request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = "The sum of " + str(num1) + ' and ' +str(num2) + " is " +str(r)
            
        if(ops == 'subtract'):
            r = num1 - num2
            result = "The difference of " + str(num1) + ' and ' +str(num2) + " is " +str(r)
            
        if(ops == 'multiply'):
            r = num1 * num2
            result = "The product of " + str(num1) + ' and ' +str(num2) + " is " +str(r)
            
        if(ops == 'divide'):
            r = num1 / num2
            result = "The division of " + str(num1) + ' and ' +str(num2) + " is " +str(r)
            
        if(ops == 'log'):
            r = math.log(num1) / math.log(num2)
            result = "The log of " + str(num1) + ' and ' +str(num2) + " is " +str(r)
        
        return render_template('results.html',result = result)

# Passing data other than form:
# using postman tool: To test APIs

@app.route('/postman_data',methods = ['POST'])  #create route as defined in html
def math_operation1():
    if(request.method == 'POST'): #If sending through form
        ops= request.json['operation']
        num1 = int(request.json['num1'])  #Data in json format
        num2 = int(request.json['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = "The sum of " + str(num1) + ' and ' +str(num2) + " is " +str(r)
            
        
        if(ops == 'subtract'):
            r = num1 - num2
            result = "The difference of " + str(num1) + ' and ' +str(num2) + " is " +str(r)
            
        if(ops == 'multiply'):
            r = num1 * num2
            result = "The product of " + str(num1) + ' and ' +str(num2) + " is " +str(r)
            
        if(ops == 'divide'):
            r = num1 / num2
            result = "The division of " + str(num1) + ' and ' +str(num2) + " is " +str(r)
           
        if(ops == 'log'):
            r = math.log(num1) / math.log(num2)
            result = "The log of " + str(num1) + ' and ' +str(num2) + " is " +str(r)
        
        return jsonify(result)  #Returns data in Json format 




if __name__=="__main__":
    app.run(host="0.0.0.0")
