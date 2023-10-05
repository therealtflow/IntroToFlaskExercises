from flask import Flask
from datetime import datetime as dt

date = Flask(__name__)

@date.route('/')
def index():
    date = dt.now()
    formatted_date = date.strftime("The Current Date Time Is %A, %B %d, %Y, %I:%M:%S %p")
    return formatted_date

if __name__ == "__main__":
    date.run(debug=True)

