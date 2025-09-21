# This is a basic Flask application that serves a static HTML file.
# The `render_template` function will look for `index.html` in a `templates` folder.

import os
from flask import Flask, render_template

app = Flask(__name__)

# Route to serve the homepage
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Use Gunicorn in production, but this is useful for local testing
    app.run(debug=True, host='0.0.0.0')
