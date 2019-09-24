from app import app
from flask import render_template, request
from app.models import model, formopener
# from formopener import dict_from

@app.route('/')
@app.route('/index')
def index():
    #render the index page to get what the user ate for breakfast
    return render_template("index.html")

@app.route('/results', methods = ['GET', 'POST'])
def results():
    #store the data from the form as the username
    username = formopener.dict_from(request.form)
    #print the userdata to the console so that I can see the dictionary
    print(username)
    #store and print the value of the breakfast to the console so that I can see it
    name = username['name']
    name = name.encode("utf-8")
    print(username['name'])
    #send the value of breakfast to the results.html page
    return render_template('results.html', name = name)
