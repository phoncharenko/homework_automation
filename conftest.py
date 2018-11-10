import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "http://pulse-rest-testing.herokuapp.com/"


@pytest.fixture()
def books_data(base_url):
    b = {"title": "Anna Karenina", "author": "Lev Tolstoy"}
    yield b
    requests.delete(base_url + "/books" + str(b["id"]))


@pytest.fixture(scope="session")
def clean_book_id(base_url):
    clean_book_id = []
    yield clean_book_id
    print(clean_book_id)
    # TODO: clean all
