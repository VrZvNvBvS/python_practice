# Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
from flask import Flask
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
# Return the string 'Hello World!' as a response

# 1 localhost:5000/ - have it say "Hello World!"
@app.route('/')
def hello_world():
    return 'Hello World!'


# 2 localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"


# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
@app.route('/say/<param>')
def say(param):
    return f"Hi {param}!"


# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
@app.route('/repeat/<param>/<int:num>')
def repeat(param, num):
    return ((param) + "\n") * num


# Ensure this file is being run directly and not from a different module
 # Run the app in debug mode.
if __name__ == "__main__":
    app.run(debug=True)
