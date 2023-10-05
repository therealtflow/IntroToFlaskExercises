#Tyler Reese Flowers
#Oct 5th 2023
#I used the videos provided in our flask prep tab on canvas
#I used W3Schools, Stack Overflow, and google for this assignment

#Import Statements
from flask import Flask, render_template, request
app = Flask(__name__)
#Defines home and returns the correct html file
@app.route('/')
def home():
    return render_template('index.html')

#Performs calculation to decide whether integer is even or odd
@app.route('/calculate')
def calc(number = None):
    if len(request.args)==0:
        return render_template('calculate.html')
    number = request.args['number']
    try:
        if int(number) %2 ==0:
            msg = 'even'
        elif int (number) %2 != 0:
            msg = 'odd'
    #Returns message if anything but integer is entered
    except:
        msg = 'not an integer'
        number = 'input'
    return render_template('calculate.html', num = number, name=msg)

#Runs application
if __name__ == "__main__":
    app.run()

