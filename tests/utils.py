from src.models import Movie, db

def refresh_db():
    Movie.query.delete()
    db.session.commit()