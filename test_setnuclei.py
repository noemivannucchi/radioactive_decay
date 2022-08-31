from hypothesis import given, strategies as st
import pytest
from setnuclei import verifynuclei

def test_k_uranium():
    d = 'Uranium238'
    assert verifynuclei(d) == 5e-18

def test_k_plutonium():
    d = 'Plutonium239'
    assert verifynuclei(d) == 9e-13
    
def test_k_radium():
    d = 'Radium226'
    assert verifynuclei(d) == 1e-11
    
def test_ValueError():
    d = 'Uranium200'   
    with pytest.raises(ValueError):
        verifynuclei(d)
        
def test_TypeError():
    d = 100  
    with pytest.raises(TypeError):
        verifynuclei(d)        