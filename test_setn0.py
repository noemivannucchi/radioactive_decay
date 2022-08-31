from hypothesis import given, strategies as st
import pytest
from setn0 import verifyN0

def test_N0_integer(): #positive test
    d = 100
    assert verifyN0(d) == d

def test_TypeError():
    d = '100'    
    with pytest.raises(TypeError):
        verifyN0(d)

def test_ValueError():
    d = -100    
    with pytest.raises(ValueError):
        verifyN0(d)

def test_zero_ValueError():
    d = 0   
    with pytest.raises(ValueError):
        verifyN0(d)