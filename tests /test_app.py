import sys
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add 
from app import subtract 
from app import multiply
from app import divide
from app import square

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_subtract():
    assert subtract(20, 15) == 5

def test_multiply():
    assert multiply(20, 15) == 300

def test_divide():
    assert divide(30, 15) == 2

def test_square():
    assert square(21) == 441

def test_squareRoot():
    assert math.sqrt(49) == 7
