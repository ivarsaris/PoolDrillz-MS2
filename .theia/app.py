import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# storing MongoDB uri and database name in variables
app.config['MONGO_DBNAME'] = 'pooldrillz'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

# opens index.html
@app.route('/')
def index():
    return render_template('index.html')

# opens exercises.html
@app.route('/exercises')
def exercises():
    return render_template('exercises.html', exercises=mongo.db.exercises.find())

# opens stats.html
@app.route('/stats')
def stats():
    return render_template('stats.html')

# opens contact.html
@app.route('/contact')
def contact():
    return render_template('contact.html')

# opens add.html
@app.route('/add')
def add():
    return render_template('add.html')

# add exercise to database
@app.route('/submit_exercise', methods=['POST'])
def submit_exercise():
    exercises = mongo.db.exercises
    exercises.insert_one(request.form.to_dict())
    return redirect(url_for('exercises'))

# opens exercise in view_exercise.html with button in exercises.html
@app.route('/view_exercise/<exercise_id>')
def view_exercise(exercise_id):
    the_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    return render_template('viewexercise.html', exercise=the_exercise)

# opens editexercise.html with 'edit exercise' button in viewexercise.html
@app.route('/edit_exercise/<exercise_id>')
def edit_exercise(exercise_id):
    the_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    return render_template('editexercise.html', exercise=the_exercise)

# updates exercise in database with form in editexercise.html
@app.route('/update_exercise/<exercise_id>', methods=["POST"])
def update_exercise(exercise_id):
    exercises = mongo.db.exercises
    exercises.update({'_id': ObjectId(exercise_id)},
    {
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'type_of_exercise': request.form.get('type_of_exercise'),
        'skill_level': request.form.get('skill_level'),
        'exercise_added_by': request.form.get('exercise_added_by'),
    })
    return redirect(url_for('exercises'))

# deletes exercise from database with button in editexercise.html
@app.route('/delete_exercise/<exercise_id>')
def delete_exercise(exercise_id):
    exercises = mongo.db.exercises
    exercises.remove({'_id': ObjectId(exercise_id)
                    })
    return redirect(url_for('exercises'))


# opens port for browser
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
