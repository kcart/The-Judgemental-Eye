"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app
from datetime import datetime


def load_users():
    """Load users from u.user into database."""
    
    users_file = open("seed_data/u.user")

    for row in users_file:
        # user_id, email, password, age, zipcode = row.split("|")
        users_info = row.strip().split("|")
        
        user_id = users_info[0]    
        email = users_info[1]    
        password = users_info[2]
        age = users_info[3]
        zipcode = users_info[4]    
        
        # user_id, email, password, age, zipcode = user_info

        #print user_id, email, password  
        user = User(user_id=user_id, email=email, password=password, age=age, zipcode=zipcode)
        #QUERY = "INSERT INTO users VALUES(user_id, email, password, age, zipcode)"
        db.session.add(user)
    
    db.session.commit()

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id, self.email)

def load_movies():
    """Load movies from u.item into database."""

    item_file= open("seed_data/u.item")

    for row in item_file:
        movie_info = row.strip().split("|")
        
        #movie_id, title, released_at, video_release_date, imdb_url = movie_info

        movie_id = movie_info[0]
        movie_title = movie_info[1]
        released_at = movie_info[2]
        imdb_url = movie_info[3]

        print movie_id , movie_title, released_at

        released_at = datetime.strptime(released_at, '%d-%b-%Y')

        movie = Movie(movie_id=movie_id, title=movie_title, released_at=released_at, imdb_url=imdb_url)
        #print released_at
        db.session.add(movie)

    db.session.commit()

def load_ratings():
    """Load ratings from u.data into database."""
    
    data_file = open("seed_data/u.data")

    for row in data_file:
        if row:
            data_info = row.strip().split()
            user_id = data_info[0]    
            movie_id = data_info[1]    
            score = data_info[2]
            timestamp = data_info[3]

            timestamp = timestamp.datetime.strptime(t_timestamp, ) #add something behind the trailing comma
                    
            rating = Rating(user_id=user_id, movie_id=t_movie_id, score=t_score, timestamp=t_timestamp)
            db.session.add(rating)
    
    db.session.commit()
   

if __name__ == "__main__":
    connect_to_db(app)

    #load_users()
    load_movies()
    #load_ratings()
