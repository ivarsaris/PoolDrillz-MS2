import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'pooldrillz'
app.config["MONGO_URI"] = 'mongodb+srv://ivars:@cluster0-q4qh1.mongodb.net/pooldrillz?retryWrites=true&w=majority'

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


# opens port for browser
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
