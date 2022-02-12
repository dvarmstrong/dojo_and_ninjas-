from flask_app import app 
from flask import render_template, redirect, session, request, flash 
from flask_app.models.dojo import Dojos




# @app.route('/')
# def index():
#     return render_template('dojo.html')

# route to create a dojo 
@app.route('/create_dojo',methods=['POST'])
def create_dojo():
    request.form
    new_dojo = Dojos.save(request.form)

    return redirect('/')

#route to display the dojos
@app.route('/')
def show_dojos():
    return render_template('dojo.html', all_dojos = Dojos.get_all())
