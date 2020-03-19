import os
from flask import Flask, render_template, redirect, request, url_for
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

# open index.html
@app.route('/')
def index():
    return render_template('index.html')

# open about.html
@app.route('/about')
def about():
    return render_template('about.html')

# add.html ##########################

# route to template
@app.route('/add')
def add():
    # opens add.html
    return render_template('add.html')

# add exercise to database
@app.route('/submit_exercise', methods=['POST'])
def submit_exercise():
    # get image from form
    image = request.files['image']
    # turn image into string
    image_string = base64.b64encode(image.read()).decode("utf-8")
    # saves values in variable
    values = request.form.to_dict()
    # turn type_of_exercise value to list so it can store multiple inputs
    values["type_of_exercise"] = request.form.getlist("type_of_exercise")
    # encode image string to save in mongo
    values["image"] = "data:image/png;base64," + image_string
    # define mongo database
    exercises = mongo.db.exercises
    # insert document in database with button in add.html
    exercises.insert_one(values)
    # return to exercises page
    return redirect(url_for('exercises'))

# exercises.html #########################

@app.route('/exercises')
def exercises():
    # define exercises as all exercises in mongo collection
    exercises = mongo.db.exercises.find()
    # opens exercises page with exercises defined
    return render_template('exercises.html', exercises=exercises)

# route for filter exercises function
@app.route('/exercises',  methods=['POST'])
# filter exercises function
def filter_exercises():
    # define exercises as all exercises in mongo collection
    exercises = mongo.db.exercises
    # get value from filter form in exercises.html
    type_filter = request.form.get('type_filter')
    # check database if there are results with this value
    try:
        doc = exercises.find({'type_of_exercise': type_filter})
    # error if can't connect to database
    except:
        print("Error accessing database!")
    # if there are results, return them in exercises template
    if doc:
        return render_template('exercises.html', exercises=doc)

# viewexercise.html #################################

@app.route('/view_exercise/<exercise_id>')
def view_exercise(exercise_id):
    # find the particular exercise in the database using its ID
    the_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    print(the_exercise)
    # opens exercise in view_exercise.html with button in exercises.html
    return render_template('viewexercise.html', exercise=the_exercise)

# editexercise.html #################################

# opens editexercise.html with 'edit exercise' button in viewexercise.html
@app.route('/edit_exercise/<exercise_id>')
def edit_exercise(exercise_id):
    # define specific exercise with its Mongo ID
    the_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    # return edit template with info of the exercise filled out
    return render_template('editexercise.html', exercise=the_exercise)

# route for update exercise function
@app.route('/update_exercise/<exercise_id>', methods=["POST"])
# update exercise function
def update_exercise(exercise_id):
    # retrieve exercises from the database
    exercises = mongo.db.exercises
    # add document to database with form
    exercise = {
        # all variables to be filled out in the form
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'type_of_exercise': request.form.getlist('type_of_exercise'),
        'skill_level': request.form.get('skill_level'),
        'date_added': request.form.get('date_added'),
        'exercise_added_by': request.form.get('exercise_added_by')
        }
    existing_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    # check if user oploaded a new image or not
    if request.files['image'].filename != '':
        # save new image
        image = request.files['image']
        # turn image into string
        image_string = base64.b64encode(image.read()).decode("utf-8")
        # save new image to database
        exercise['image'] = "data:image/png;base64," + image_string
    else:
        # keep using existing image if no new image is given
        exercise['image'] = existing_exercise['image']
    # add document to database with form
    exercises.update({"_id": ObjectId(exercise_id)}, exercise)
    # redirect to exercises page after updating exercises
    return redirect(url_for('exercises'))

# route for delete exercise function
@app.route('/delete_exercise/<exercise_id>')
# delete exercise function
def delete_exercise(exercise_id):
    # define exercises
    exercises = mongo.db.exercises
    # delete exercise from database with button
    exercises.remove({"_id": ObjectId(exercise_id)
                      })
    # open exercises page after deleting exercise
    return redirect(url_for('exercises'))

# stats.html ######################################

# opens stats page
@app.route('/stats')
def stats():
    # define the exercises in the database
    exercises = mongo.db.exercises
    # count amount of exercises
    amount_of_exercises = exercises.count()
    # sort exercises by date added, return in descending order
    exerc_sorted_date = exercises.find().sort("date_added", -1)
    # find exercise last added
    last_aded_exerc = exerc_sorted_date[0]
    # render template with the variables
    return render_template('stats.html', amount_of_exercises=amount_of_exercises,
                           last_aded_exerc=last_aded_exerc)


# opens port for browser
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=False)
