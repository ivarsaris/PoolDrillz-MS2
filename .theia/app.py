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

# add task to database with submit button
@app.route('/add', methods=['POST'])
def submit_exercise():
    exercises = mongo.db.exercises
    exercises.insert_one(request.form.to_dict())
    return redirect(url_for('exercises'))


# opens port for browser
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
