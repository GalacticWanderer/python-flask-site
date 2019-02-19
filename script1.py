from flask import Flask, render_template  # import flask

# assigning a name to the flask app. __name__ gets turned into __main__
# when executed
app = Flask(__name__)

# the root directory of the site
@app.route('/')  # accessible at http://localhost:5000/
# funcs for home page
def home():
    # returns a render_template from the templates folder
    return render_template("home.html")


# the home directory of the site
@app.route('/about')  # accessible at http://localhost:5000/about
# funcs for about page
def about():
    # returns a render_template from the templates folder
    return render_template("about.html")


# running the app with debug mode
if __name__ == "__main__":
    app.run(debug=True)

# before you deploy any app or do any web projects, be sure to make a virtual
# environment for python
