"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db



app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route('/loginpage')
def loginpage():
    """Login/Signup page"""

    #add username and password to database
    username = request.form.get("username")
    password = request.form.get("password")

    # get the user with this email
    # check if this is the right password
    # no? flash failure message, redirect to login form
    # yes?  put something in session:    session['logged_in_user']=userid 

    #  check username and password in db
    # if username and password in db(and statment):
        # yes?  put something in session:    session['logged_in_user']=userid
    if session.query(Users).filter_by(username=userid, password=password):
        flash("You've successfully registered.")
        session['logged_in_user']=userid
    else:
        flash("You haven't registered")


    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'
  


@app.route('/loginpage', methods=["POST"])
def login_submission():
    """handles login submission"""
    #if credentials already exist in database, flash logged in message.
    #if credentials don't match the database, return failed message
    #not allow duplicate emails 



    return render_template("homepage.html")


@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()