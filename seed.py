"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app
from datetime import datetime


def load_users():
    """Load users from u.user into database."""

    users_file = open("seed_data/u.user")

    for row in users_file:
        user_id, age, gender, job, zipcode = row.split("|")
        user = User(user_id=user_id,
                    age=age,
                    zipcode=zipcode)

        db.session.add(user)
    db.session.commit()

def load_movies():
    """Load movies from u.item into database."""

    item_file= open("seed_data/u.item")

    for row in item_file:
        movie_info = row.strip().split("|")

        movie_id = movie_info[0]
        movie_title = movie_info[1]

        for movie in movie_title:
            movie = movie_title.split()
            del movie[-1]
            movie_no_year = " ".join(movie)
        print movie_no_year
  
        released_at = movie_info[2]
        imdb_url = movie_info[3]
        
        if released_at:
           released_at = datetime.strptime(released_at, '%d-%b-%Y')

        else:
            released_at = None

        movie_data = Movie(movie_id=movie_id,
                            title=movie_no_year, 
                            released_at=released_at, 
                            imdb_url=imdb_url)
    
        db.session.add(movie_data)

    db.session.commit()

def load_ratings():
    """Load ratings from u.data into database."""
    
    for i, row in enumerate(open("seed_data/u.data")):
        row = row.rstrip()

        user_id, movie_id, score, timestamp = row.split("\t")

        user_id = int(user_id)
        movie_id = int(movie_id)
        score = int(score)

        rating = Rating(user_id=user_id,
                        movie_id=movie_id,
                        score=score)

        db.session.add(rating)

        if i % 1000 == 0:
            print i

            db.session.commit()
   

if __name__ == "__main__":
    connect_to_db(app)

    load_users()
    load_movies()
    load_ratings()

    eye = User(email="the-eye@of-judgment.com", password="evil")
    db.session.add(eye)
    db.session.commit()

    # Toy Story
    r = Rating(user_id=eye.user_id, movie_id=1, score=6)
    db.session.add(r)

    # Robocop 3
    r = Rating(user_id=eye.user_id, movie_id=1274, score=5)
    db.session.add(r)

    # Judge Dredd
    r = Rating(user_id=eye.user_id, movie_id=373, score=2)
    db.session.add(r)

    # 3 Ninjas
    r = Rating(user_id=eye.user_id, movie_id=314, score=5)
    db.session.add(r)

    # Aladdin
    r = Rating(user_id=eye.user_id, movie_id=95, score=4)
    db.session.add(r)

    # The Lion King
    r = Rating(user_id=eye.user_id, movie_id=71, score=6)
    db.session.add(r)

    db.session.commit()


    moshe = User(email="moshe@gmail.com",
                   password="ari",
                   age=42,
                   zipcode="94109")
    db.session.add(jessica)
    db.session.commit()

    # Toy Story
    r = Rating(user_id=moshe.user_id, movie_id=1, score=5)
    db.session.add(r)

    # Robocop 3
    r = Rating(user_id=moshe.user_id, movie_id=1274, score=1)
    db.session.add(r)

    # Judge Dredd
    r = Rating(user_id=moshe.user_id, movie_id=373, score=1)
    db.session.add(r)

    # 3 Ninjas
    r = Rating(user_id=moshe.user_id, movie_id=314, score=1)
    db.session.add(r)

    # Aladdin
    r = Rating(user_id=moshe.user_id, movie_id=95, score=5)
    db.session.add(r)

    # The Lion King
    r = Rating(user_id=moshe.user_id, movie_id=71, score=5)
    db.session.add(r)

    db.session.commit()
