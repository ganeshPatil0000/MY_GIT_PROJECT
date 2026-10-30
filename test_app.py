from app import greet
from app import add

def test_greet():
    assert "Ganesh" in greet("Ganesh")

def test_add():
    assert add(2, 3) == 5
    