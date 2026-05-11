from app import app, db, Genre, Movie

with app.app_context():
    # Clear previous data
    db.drop_all()
    db.create_all()

    # Add genres
    action = Genre(name="Action")
    thriller = Genre(name="Thriller")
    romance = Genre(name="Romance")
    horror = Genre(name="Horror")
    sci_fi = Genre(name="Sci-Fi")
    comedy = Genre(name="Comedy")
    drama = Genre(name="Drama")

    db.session.add_all([action, thriller, romance, horror, sci_fi, comedy, drama])
    db.session.commit()

    # Add movies
    movies = [
        Movie(title="Inception", description="A mind-bending thriller", release_year=2010, genre=thriller, poster_filename="inception.jpg"),
        Movie(title="Interstellar", description="Journey through space and time", release_year=2014, genre=sci_fi, poster_filename="interstellar.jpg"),
        Movie(title="The Dark Knight", description="Batman faces the Joker", release_year=2008, genre=action, poster_filename="darkknight.jpg"),
        Movie(title="Titanic", description="Epic romance aboard the doomed ship", release_year=1997, genre=romance, poster_filename="titanic.jpg"),
        Movie(title="Joker", description="A man’s descent into madness", release_year=2019, genre=drama, poster_filename="joker.jpg"),
        Movie(title="The Hangover", description="A wild bachelor party in Vegas", release_year=2009, genre=comedy, poster_filename="hangover.jpg"),
        Movie(title="Deadpool", description="A witty anti-hero’s origin", release_year=2016, genre=action, poster_filename="deadpool.jpg"),
        Movie(title="Get Out", description="A chilling social horror", release_year=2017, genre=horror, poster_filename="getout.jpg"),
        Movie(title="Parasite", description="A tale of class struggle", release_year=2019, genre=drama, poster_filename="parasite.jpg"),
        Movie(title="Superbad", description="Teen comedy chaos", release_year=2007, genre=comedy, poster_filename="superbad.jpg"),
        Movie(title="The Notebook", description="An enduring love story", release_year=2004, genre=romance, poster_filename="notebook.jpg"),
        Movie(title="A Quiet Place", description="Silence is survival", release_year=2018, genre=horror, poster_filename="quietplace.jpg"),
        Movie(title="Shutter Island", description="A twisted psychological thriller", release_year=2010, genre=thriller, poster_filename="shutterisland.jpg"),
        Movie(title="Avengers: Endgame", description="Heroes unite to reverse the snap", release_year=2019, genre=action, poster_filename="avengersendgame.jpg"),
        Movie(title="Her", description="A man falls for an AI", release_year=2013, genre=romance, poster_filename="her.jpg"),
    ]

    db.session.add_all(movies)
    db.session.commit()

    print("✅ Database seeded successfully with genres and 15 movies.")
