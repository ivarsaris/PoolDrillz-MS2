import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from base64 import b64encode
from bson.json_util import dumps, loads
import base64

app = Flask(__name__)

# storing MongoDB uri and database name in variables
app.config['MONGO_DBNAME'] = 'pooldrillz'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# add.html ##########################

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/submit_exercise', methods=['POST'])
def submit_exercise():
    """
    Add exercise to the database
    """
    image = request.files['image']
    
    # turn image into string
    image_string = base64.b64encode(image.read()).decode("utf-8")

    values = request.form.to_dict()
    
    # turn type_of_exercise value to list so it can store multiple inputs
    values["type_of_exercise"] = request.form.getlist("type_of_exercise")
    
    # encode image string to save in mongo
    values["image"] = "data:image/png;base64," + image_string

    """
    check if user added valid name, needs to be longer than 3
    and shorter than 30 characters. If not, page is reloaded with
    warning message
    """
    name = request.form.get("name")

    if len(name) < 3 or len(name) > 30:
        flash("Please submit a name of more than 3, and less than 30 characters.", "warning")
        return redirect(url_for('add'))

    """
    Check is user added description of more than 10 characters.
    If not, page is reloaded with warning message 
    """
    description = request.form.get("description")

    if len(description) <= 10:
        flash("Please add a description of more than 10 characters to the exercise", "warning")
        return redirect(url_for('add'))

    """
    Check if user added a type of exercise.
    If not, page is reloaded with warning message 
    """
    type_of_exercise = request.form.getlist("type_of_exercise")

    if len(type_of_exercise) < 1:
        flash("Please choose one or more skill types.", "warning")
        return redirect(url_for('add'))
    
    """
    Check if user added a skill level.
    If not, page is reloaded with warning message 
    """
    skill_level = request.form.get("skill_level")

    if not skill_level:
        flash("Please select a difficulty level", "warning")
        return redirect(url_for('add'))

    """
    Check if user added a data.
    If not, page is reloaded with warning message 
    """
    date_added = request.form.get("date_added")

    if not date_added:
        flash("Please select a date.", "warning")
        return redirect(url_for('add'))

    """
    Check if user added their name.
    If not, page is reloaded with warning message
    """
    user_name = request.form.get("exercise_added_by")

    if not user_name:
        flash("Please give your name.", "warning")

    exercises = mongo.db.exercises

    exercises.insert_one(values)

    flash("Exercise succesfully submitted to the database!", "success")
    
    return redirect(url_for('exercises'))

# exercises.html #########################

@app.route('/exercises')
def exercises():
    """
    open exercises page and retrieve all
    exercises from the database
    """
    exercises = mongo.db.exercises.find()
    
    return render_template('exercises.html', exercises=exercises)

@app.route('/exercises',  methods=['POST'])
def filter_exercises():
    """
    Filter the exercises by type of exercise. Retrieve all
    exercises and check which ones have a certain 'type'.
    return these in the exercises template
    """
    exercises = mongo.db.exercises
    type_filter = request.form.get('type_filter')

    """
    If a filter returns 0 results, open exercises template
    and display message
    """
    doc = exercises.find({'type_of_exercise': type_filter})
    if doc.count_documents({}) == 0:
        flash("No exercises of this type", "warning")
        return redirect(url_for('exercises'))

    return render_template('exercises.html', exercises=doc)

# viewexercise.html #################################

@app.route('/view_exercise/<exercise_id>')
def view_exercise(exercise_id):
    """
    find the particular exercise in the database using its ID
    """
    the_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    
    return render_template('viewexercise.html', exercise=the_exercise)

# editexercise.html #################################

# opens editexercise.html with 'edit exercise' button in viewexercise.html
@app.route('/edit_exercise/<exercise_id>')
def edit_exercise(exercise_id):
    """
    open the edit exercise template with a specific exercises' 
    information using its mongo ID
    """
    the_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})

    return render_template('editexercise.html', exercise=the_exercise)

@app.route('/update_exercise/<exercise_id>', methods=["POST"])
def update_exercise(exercise_id):
    """
    open the edit exercise template with a specific exercises' 
    information using its mongo ID
    """
    exercises = mongo.db.exercises
    exercise = {
        'name': request.form.get('name'),        
        'description': request.form.get('description'),
        'type_of_exercise': request.form.getlist('type_of_exercise'),
        'skill_level': request.form.get('skill_level'),
        'date_added': request.form.get('date_added'),
        'exercise_added_by': request.form.get('exercise_added_by')
        }
    existing_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    """
    check if user oploaded a new image or not. if they did,
    upload new picture, if not, keep using existing image.
    """
    if request.files['image'].filename != '':
        image = request.files['image']
        # code image into string to save it to database
        image_string = base64.b64encode(image.read()).decode("utf-8")
        exercise['image'] = "data:image/png;base64," + image_string
    else:
        exercise['image'] = existing_exercise['image']

    exercises.replace_one({"_id": ObjectId(exercise_id)}, exercise)

    flash("Exercise updated successfully", "success")

    return redirect(url_for('exercises'))

@app.route('/delete_exercise/<exercise_id>')
def delete_exercise(exercise_id):
    """  
    delete exercise from database with button
    in edit exercise page.
    """ 
    exercises = mongo.db.exercises
    exercises.remove({"_id": ObjectId(exercise_id)
                      })

    flash("Exercise succesfully deleted from the database.", "success")
    
    return redirect(url_for('exercises'))

# stats.html ######################################

# opens stats page
@app.route('/stats')
def stats():
    exercises = mongo.db.exercises
    amount_of_exercises = exercises.count_documents({})
    """
    sort exercises by date added, return in ascending order.
    find exercise last added
    """
    exerc_sorted_date = exercises.find().sort("date_added", -1)
    last_aded_exerc = exerc_sorted_date[0]

    return render_template('stats.html', amount_of_exercises=amount_of_exercises,
                           last_aded_exerc=last_aded_exerc)


# opens port for browser
if __name__ == "__main__":
    app.secret_key = 'pooldrillzqwerty'
    app.run(host="0.0.0.0",
            port=int("8080"),
            debug=True)

# if __name__ == "__main__":
    # app.run(host=os.environ.get("IP"),
    #         port=os.environ.get("PORT"),
    #         debug=False)