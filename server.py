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

@app.route('/loginpage', methods=["POST", "GET"])
def login_submission():
    """handles login submission"""
    if request.method == "POST":
        username = request.form["username_input"]
        password = request.form["password_input"]
        user_object = User.query.filter(User.email == username).first()
        #if credentials already exist in database, flash logged in message.
        #if credentials don't match the database, return failed message
        #not allow duplicate emails 
        # we should probably look at validating and user with the email?
        print user_object
        if user_object:
            if user_object.password == password:
                session["login"] = username
                flash("You've successfully logged in.")
                return redirect("/")
            else:
                flash("Wrong Login.")
                return redirect("/loginpage")
        else:
            flash("Your username is not on file")
            return redirect("/loginpage")
            

    return render_template("/loginpage.html")
# return render_template("/loginpage.html")
@app.route('/loginpage')
def loginpage():
    """Login/Signup page"""

    #add username and password to database


    # get the user with this email
    # check if this is the right password
    # no? flash failure message, redirect to login form
    # yes?  put something in session:    session['logged_in_user']=userid 

     # check username and password in db
    # if username and password in db(and statment):
    #     yes?  put something in session:    session['logged_in_user']=userid
    # if db.session.query(User).filter_by(user_id= username_input, password=password_input):
    #     flash("You've successfully registered.")
    #     session['logged_in_user']=username_input
    # else:
    #     flash("You haven't registered.")
    #     return redirect("/")

    # if 'username' in session:
    #     return 'Logged in as %s' % escape(session['username'])
    return render_template("loginpage.html")

@app.route('/loginout', methods=["POST", "GET"])
def loginout():
    """Loginout page"""

    flash("You have been successfully logged out.")

    session.pop('login')

    return render_template("/homepage.html")

@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/users/<int:id>")
def user_detaiL(id):
    """ Shows the age, zipcode, movies that the user rated, and the scores they rated the movies"""

    print "*" * 20
    
    print "*" * 20

    user = User.query.get(id)
    print user 
   
    return render_template("user_details.html", user=user)

@app.route("/movies")
def movie_list():
    """ Making a page that shows all the information about a specific movie, including all ratings that the movie has received"""

    movies = Movie.query.all()

    print "*" * 20
    print movies
    print "*" * 20
    

    return render_template("movie_list.html", movies=movies)

@app.route("/movies_ratings")
def movie_rating():
    """Add new ratings and edit ratings for movies. """
    
    score = int(request.form["score"])

    user_id = session.get("user_id")

    if not user_id:
        raise Exception("You're not logged in.")
        
    rating = Rating.query.filter_by(user_id=user_id, movie_id=movie_id).first() 

    #for existing ratings
    if rating:
        ratings.score = score 
        flash("You've successfully updated your rating.")


    else: #new ratings
        (ratings.score, movie.id)
        
        rating = Rating(user_id=user_id, movie_id=movie_id, score=score)
        flash("You've successfully created a new rating.") 
        db.session.add(rating)

    db.session.commit()

    return redirect("/movies/%s" %s movie_id)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()