from flask_app import app 
from flask import render_template, redirect, session, request, flash 
from flask_app.models import dojo
from flask_app.models.ninja import Ninja





@app.route('/ninjas')
def new_ninja():
    dojo_from_db =dojo.Dojos.get_all()
    return render_template("new_ninja.html", all_dojos = dojo_from_db)



@app.route('/create_ninja', methods=['POST'])
def add():
    

    Ninja.save(request.form)
    print('data')
    return redirect('/ninjas')

    