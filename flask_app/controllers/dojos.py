from flask_app import app 
from flask import render_template, redirect, session, request, flash 
from flask_app.models.dojo import Dojos




# route to create a dojo 
@app.route('/create_dojo',methods=['POST'])
def create_dojo():

        new_dojo = Dojos.save(request.form)
        return redirect('/')




#route to display the dojos
@app.route('/')
def show_dojos():
        return render_template('dojo.html', all_dojos = Dojos.get_all())


@app.route('/show/dojo/<int:dojo_id>')
def show(dojo_id):
        info_dict = {
                'id': dojo_id
        }
        this_dojo = Dojos.get_dojo_and_ninjas(info_dict)
        return render_template('dojo_show.html', this_dojo = this_dojo )




