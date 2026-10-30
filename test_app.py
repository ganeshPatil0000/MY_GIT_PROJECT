from app import greet
from utils import add

def test_greet():
    assert "Ganesh" in greet("Ganesh")

def test_add():
    assert add(2, 3) == 5
    