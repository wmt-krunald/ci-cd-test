# test_app.py
from hello import hangman


def test_hello():
    
    response = hangman.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'word.upper()'
