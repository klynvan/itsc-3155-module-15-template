from flask.testing import FlaskClient

from app import app
from src.models import Movie, db

def test_get_all_movies(test_app: FlaskClient):
    with app.app_context():
        # setup
        test_movie = Movie(title='Minions', director='Kyle Balda', rating=4)
        db.session.add(test_movie)
        db.session.commit()


        #run action
        res = test_app.get('/movies')
        page_data: str = res.data.decode()

        #asserts
        assert res.status_code == 200
        assert '<td><a href="/movies/{{ movie.movie_id }}">Minions</a></td>' in page_data
        assert ' <td>Kyle Balda</td>' in page_data
        assert ' <td>4</td>' in page_data