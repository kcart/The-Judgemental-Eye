"""Utility file to seed ratings database from MovieLens data in seed_data/"""

import datetime

from model import User, Rating, Movie, connect_to_db, db
from server import app


def load_users():
    """Load users from u.user into database."""

    print "Users"

    for i, row in enumerate(open("seed_data/u.user")):
        row = row.rstrip()
        user_id, age, gender, occupation, zipcode = row.split("|")

        user = User(user_id=user_id,
                    age=age,
                    zipcode=zipcode)


        db.session.add(user)

    db.session.commit()


def load_movies():
    """Load movies from u.item into database."""

    print "Movies"

    for i, row in enumerate(open("seed_data/u.item")):
        row = row.rstrip()


        movie_id, title, released_str, junk, imdb_url = row.split("|")[:5]

        if released_str:
            released_at = datetime.datetime.strptime(released_str, "%d-%b-%Y")
        else:
            released_at = None



        title = title[:-7] 

        movie = Movie(movie_id=movie_id,
                      title=title,
                      released_at=released_at,
                      imdb_url=imdb_url)


        db.session.add(movie)



    db.session.commit()


def load_ratings():
    """Load ratings from u.data into database."""

    print "Ratings"

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

        db.session.commit()


    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users()
    load_movies()
    load_ratings()

    eye = User(email="the-eye@of-judgment.com", password="evil")
    db.session.add(eye)
    db.session.commit()

    # Toy Story
    r = Rating(user_id=eye.user_id, movie_id=1, score=1)
    db.session.add(r)

    # Robocop 3
    r = Rating(user_id=eye.user_id, movie_id=1274, score=5)
    db.session.add(r)

    # Judge Dredd
    r = Rating(user_id=eye.user_id, movie_id=373, score=5)
    db.session.add(r)

    # 3 Ninjas
    r = Rating(user_id=eye.user_id, movie_id=314, score=5)
    db.session.add(r)

    # Aladdin
    r = Rating(user_id=eye.user_id, movie_id=95, score=1)
    db.session.add(r)

    # The Lion King
    r = Rating(user_id=eye.user_id, movie_id=71, score=1)
    db.session.add(r)

    db.session.commit()
    
    # Add our user
    moshe = User(email="moseh@gmail.com",
                   password="ocean",
                   age=42,
                   zipcode="94109")
    db.session.add(moshe)
    db.session.commit()

    # Toy Story
    r = Rating(user_id=jessica.user_id, movie_id=1, score=5)
    db.session.add(r)

    # Robocop 3
    r = Rating(user_id=jessica.user_id, movie_id=1274, score=1)
    db.session.add(r)

    # Judge Dredd
    r = Rating(user_id=jessica.user_id, movie_id=373, score=1)
    db.session.add(r)

    # 3 Ninjas
    r = Rating(user_id=jessica.user_id, movie_id=314, score=1)
    db.session.add(r)

    # Aladdin
    r = Rating(user_id=jessica.user_id, movie_id=95, score=5)
    db.session.add(r)

    # The Lion King
    r = Rating(user_id=jessica.user_id, movie_id=71, score=5)
    db.session.add(r)

    db.session.commit()
