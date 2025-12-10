import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add 
from app import subtract 
from app import multiply

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_subtract():
    assert subtract(20, 15) == 5

def test_multiply():
    assert multiply(20, 15) == 300
