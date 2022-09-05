from hypothesis import given, strategies as st
import pytest
from setn0 import verifyN0

#===========================
#PROPERTY TESTING 
#===========================

@given(N0 = st.integers(min_value = 0))
def test_good_values_h(N0):
    if N0 != 0:
       assert verifyN0(N0) == N0

@given(N0 = st.text())
def test_TypeError_h(N0):
    with pytest.raises(TypeError):
        verifyN0(N0)

@given(N0 = st.integers(max_value = 0))
def test_ValueError_h(N0):
    with pytest.raises(ValueError):
        verifyN0(N0)

@given(N0 = st.just(0))
def test_zero_ValueError_h(N0):
    with pytest.raises(ValueError):
        verifyN0(N0)

#===========================
#UNIT TESTING 
#all the possible positive and negative combinations
#===========================

def test_N0_integer(): 
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
