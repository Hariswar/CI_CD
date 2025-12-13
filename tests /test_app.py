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
from app import square_root
from app import math_sin
from app import math_cos
from app import percentage

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
    assert square_root(49) == 7

def test_sin():
    assert math_sin(0) == 0

def test_cos():
    assert math_cos(0) == 1

def test_pecentage():
    assert percentage(400, 1000) == 40
