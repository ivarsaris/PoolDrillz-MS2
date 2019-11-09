import os
from flask import Flask, render_template

app = Flask(__name__)

# opens index.html
@app.route('/')
def index():
    return render_template('index.html')

# opens exercises.html
@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

# opens stats.html
@app.route('/stats')
def stats():
    return render_template('stats.html')

#opens contact.html
@app.route('/contact')
def contact():
    return render_template('contact.html')

# opens port for browser
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
