#Tyler R Flowers
#October 5th 2023
#I used the videos provided in the flask ex prep section
#I used W3 Schools, Stack Overflow, and Geeks for geeks to complete this assignment
#I used getbootstrap.com for the bootstrap template in this assignment

#import-statements
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#array of registered users
registered_users = {}

#array of 5 organizations
organizations = ['code9','Charlotte Hack','Charlotte Financial','Charlotte Boxing','Dog Lovers']

#sets up home page, allowing users to enter a name and pick an organization
@app.route('/', methods=['GET', 'POST'])
def home():
    #if both entered values are correct submit the form 
    if request.method == 'POST':
        name = request.form.get('name')
        organization = request.form.get('organization')

        #if there is either no name entered or no organization selected return error statement
        if not name or not organization:
            error = 'Both Name and Organization are required fields.'
            return render_template('home.html', organizations=organizations, error=error)
        
        #if the organization selected is not a valid organization return error statement
        if organization not in organizations:
            error = 'Invalid organization selected.'
            return render_template('home.html', organizations=organizations, error=error)
        
        registered_users[name] = organization

        #redirects to the registered.html tab
        return redirect(url_for('registered'))
    
    return render_template('home.html', organizations=organizations)

#renders template for registered tab of all registered users
@app.route('/registered')
def registered():
    return render_template('registered.html', registered_users=registered_users)

if __name__ == '__main__':
    app.run(debug=True) 