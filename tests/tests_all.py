# tests/test_lib.py
from disintegration.lib import try_me


def test_length_of_hello_world():
    assert try_me() == 'successful disintegration'
