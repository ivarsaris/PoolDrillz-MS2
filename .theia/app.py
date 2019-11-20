import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# storing MongoDB uri and database name in variables
app.config['MONGO_DBNAME'] = 'pooldrillz'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

# open index.html
@app.route('/')
def index():
    return render_template('index.html')

# open contact.html
@app.route('/contact')
def contact():
    return render_template('contact.html')

# add.html

# route to template
@app.route('/add')
def add():
    # opens add.html
    return render_template('add.html')

# add exercise to database
@app.route('/submit_exercise', methods=['POST'])
def submit_exercise():
    # check if an image file has been addded
    if 'image' in request.files:
        # store image input in form in variable
        image = request.files['image']
        # save image to exercises database
        mongo.save_file(image.filename, image)
    # define the documents in the database(the exercises)
    exercises = mongo.db.exercises
    # insert document in database with button in add.html
    exercises.insert_one(request.form.to_dict())
    # redirect to exercises page after adding exercise to database
    return redirect(url_for('exercises'))

# function to be able to show image in webpage
@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

# exercises.html


@app.route('/exercises')
def exercises():
    # define exercises as all exercises in mongo collection
    exercises = mongo.db.exercises.find()
    # define specific exercise
    # exercise = mongo.db.exercises.find_one({'name': name})
    # opens exercises page with exercises defined
    return render_template('exercises.html', exercises=exercises)


@app.route('/view_exercise/<exercise_id>')
def view_exercise(exercise_id):
    # find the particular exercise in the database using its ID
    the_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    # opens exercise in view_exercise.html with button in exercises.html
    return render_template('viewexercise.html', exercise=the_exercise)

# viewexercise.html

# opens editexercise.html with 'edit exercise' button in viewexercise.html
@app.route('/edit_exercise/<exercise_id>')
def edit_exercise(exercise_id):
    the_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    return render_template('editexercise.html', exercise=the_exercise)

# editexercise.html

# route for update exercise function
@app.route('/update_exercise/<exercise_id>', methods=["POST"])
# update exercise function
def update_exercise(exercise_id):
    # retrieve exercises from the database
    exercises = mongo.db.exercises
    # add document to database with form
    exercises.update({'_id': ObjectId(exercise_id)},
    {
        # all variables to be filled out in the form
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'type_of_exercise': request.form.get('type_of_exercise'),
        'skill_level': request.form.get('skill_level'),
        'date_added': request.form.get('date_added'),
        'exercise_added_by': request.form.get('exercise_added_by'),
    })
    # redirect to exercises page after updating exercises
    return redirect(url_for('exercises'))

# route for delete exercise function
@app.route('/delete_exercise/<exercise_id>')
# delete exercise function
def delete_exercise(exercise_id):
    # define exercises
    exercises = mongo.db.exercises
    # delete exercise from database with button
    exercises.remove({'_id': ObjectId(exercise_id)
                    })
    # open exercises page after deleting exercise
    return redirect(url_for('exercises'))


# stats.html

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
            debug=True)
