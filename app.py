from flask import Flask, render_template

app = Flask(__name__)

# Creating an app instance

# Use a decorator @ to define the route for our webpage
@app.route("/")
# Setting a default page

def index():
    return "Welcome to DevOps team"

@app.route("/welcome/")
def welcome():
    return f"Welcome to my webpage"

@app.route("/home/")
def home():
    return render_template("index.html")

# create 2 more pages/ routes add the functionality for email and password
# implement OOP inheritance

if __name__ == "__main__":
    app.run(debug=True)
