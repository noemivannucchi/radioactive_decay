from hypothesis import given, strategies as st
import pytest
from setnuclei import verifynuclei

#===========================
#PROPERTY TESTING 
#===========================

@given(d = st.just('Uranium238'))
def test_k_uranium_h(d):
    assert verifynuclei(d) == 5e-18
    
@given(d = st.just('Plutonium239'))
def test_k_plutonium_h(d):
    assert verifynuclei(d) == 9e-13

@given(d = st.just('Radium226'))
def test_k_radium_h(d):
    assert verifynuclei(d) == 1e-11

@given(d = st.characters())
def test_ValueError_h(d):
    if d !='Uranium238' and d !='Plutonium239' and d !='Radium226':
     with pytest.raises(ValueError):
        verifynuclei(d)
        
@given(d = st.fractions())
def test_TypeError_h(d):
     with pytest.raises(TypeError):
        verifynuclei(d)     

@given(d = st.just('Uranium238'))
def test_result_float_h(d):
    assert isinstance(verifynuclei(d) , float)  

#===========================
#UNIT TESTING 
#all the possible positive and negative combinations
#===========================

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
        
def test_result_float(): 
    d = 'Radium226'
    assert isinstance(verifynuclei(d) , float)        
