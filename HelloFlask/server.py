# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    # Return the string 'Hello World!' as a response
    return render_template('index.html')

@app.route('/show/<word>/int:word')


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
