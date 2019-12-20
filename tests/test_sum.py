from http import HTTPStatus
from pytest import fixture
from app.models.library import Book, Litterateur


def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == HTTPStatus.OK, 'check failed'
    # assert response.json == {'message': 'Healthy'}, 'Improper response'
#
def test_get_book(client):
    response = client.get('/book/1')
    assert response.status_code == HTTPStatus.OK, 'check failed'
