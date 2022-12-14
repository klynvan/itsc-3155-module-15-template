from flask.testing import FlaskClient

from src.models import Movie, db
from tests.utils import refresh_db


def test_get_all_movies(test_app: FlaskClient):
    # setup
    test_movie = Movie(title='Minions', director='Kyle Balda', rating=4)
    db.session.add(test_movie)
    db.session.commit()

    # run action
    res = test_app.get('/movies')
    page_data: str = res.data.decode()

    # asserts
    assert res.status_code == 200
    assert f'<td><a href="/movies/{test_movie.movie_id}">Minions</a></td>' in page_data
    assert ' <td>Kyle Balda</td>' in page_data
    assert ' <td>4</td>' in page_data


def test_get_all_movies_empty(test_app: FlaskClient):
    refresh_db()

    Movie.query.delete()
    db.session.commit()

    res = test_app.get('/movies')
    page_data: str = res.data.decode()

    assert res.status_code == 200
    assert '<td>' not in page_data


def test_get_single_movie_404(test_app: FlaskClient):
    refresh_db()

    res = test_app.get('/movie/1')

    assert res.status_code == 404


# def test_create_movie(test_app: FlaskClient):
    # refresh_db()

    # res = test_app.post('/movies', data={
    # 'title': 'The Dark Knight',
    # 'director': 'Christopher',
    # 'rating': 5,
    # }, follow_redirect=True)
    #page_data = res.data.decode()

    #assert res.status_code == 200
    #assert '<h1> The Dark Knight - 4 </h1>' in page_data
    #assert '<h2> Christopher Nolan</h2>' in page_data
