# Movie Recommendation System

A simple Flask web app for browsing movies, registering users, rating movies, and viewing a basic recommendations page. The app uses SQLite through Flask-SQLAlchemy and includes poster assets for the seeded movie catalog.

## Description

The Movie Recommendation System is a beginner-friendly web application that lets users create an account with a username, explore a catalog of movies, and rate each movie from 1 to 5. Each movie includes a title, short description, release year, genre, and poster image.

The app stores users, movies, genres, and ratings in a local SQLite database. A seed script is included to quickly populate the database with sample genres and 15 popular movies. The recommendations page currently shows a simple list of movies from the database, making it a good starting point for building a more advanced personalized recommendation algorithm later.

## Features

- User registration and login with a username
- Movie dashboard with posters, descriptions, release years, and genres
- 1-5 star-style movie ratings per user
- Basic recommendations page showing a small set of movies
- SQLite database setup through Flask-SQLAlchemy
- Seed script with 15 sample movies and genres

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML/CSS with Jinja templates

## Project Structure

```text
.
+-- app.py                  # Main Flask app, models, routes, and database setup
+-- seed_data.py            # Rebuilds and seeds the database with sample movies
+-- instance/               # SQLite database files used by Flask
+-- static/
|   +-- styles.css          # App styling
|   +-- images/posters/     # Movie poster images
+-- templates/              # Jinja HTML templates
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
pip install Flask Flask-SQLAlchemy
```

## Seed the Database

Run the seed script to create the tables and add sample genres and movies:

```powershell
python seed_data.py
```

This script drops the existing tables and recreates them, so any registered users or ratings will be removed.

## Run the App

Start the Flask development server:

```powershell
python app.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000
```

## How to Use

1. Register a username.
2. Browse the movie dashboard.
3. Rate movies from 1 to 5.
4. Open the recommendations page to see suggested movies.
5. Logout when finished.

## Important Notes

- The app currently uses username-only authentication. There are no passwords.
- The recommendation route currently returns the first five movies from the database.
- The Flask secret key is hardcoded in `app.py`, which is acceptable for local practice but should be moved to an environment variable before any real deployment.
- Poster filenames in the database must match files in `static/images/posters/`.

## Possible Improvements

- Add password-based authentication
- Generate personalized recommendations based on user ratings
- Add movie detail pages to the dashboard flow
- Add search and genre filters
- Move configuration into environment variables
- Add a `requirements.txt` file for repeatable installs
