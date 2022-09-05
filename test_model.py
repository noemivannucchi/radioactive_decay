from model import model
from hypothesis import given
from hypothesis import strategies as st
import pytest
import numpy as np

#===========================
#PROPERTY TESTING 
#===========================

@given(k = st.floats(min_value = 0,exclude_min = True), N = st.floats(min_value = 0,exclude_min = True), t = st.floats(min_value = 0,exclude_min = True) )
def test_good_values_h(N,k,t):
    assert isinstance(model(N,t,k) , float) 

@given(k = st.text(), N = st.floats(min_value = 0,exclude_min = True), t = st.floats(min_value = 0,exclude_min = True) )
def test_TypeError_k_h(N,k,t):
    with pytest.raises(TypeError):
         model(N,t,k)

@given(k = st.floats(min_value = 0,exclude_min = True), N = st.floats(max_value = 0, exclude_max = True), t = st.floats(min_value = 0,exclude_min = True) )
def test_ValueError_N_h(N,k,t):
    with pytest.raises(ValueError):
         model(N,t,k)

@given(k = st.floats(max_value = 0),  N = st.floats(min_value = 0,exclude_min = True), t = st.floats(min_value = 0,exclude_min = True) )
def test_ValueError_k_h(N,k,t):
    with pytest.raises(ValueError):
         model(N,t,k)

#===========================
#UNIT TESTING 
#all the possible positive and negative combinations
#===========================

def test_k_float(): 
    """positive test that check if the 'model' function works 
    when k is a float value
    """
    #define variables for the input of 'model' function with k decimal
    k = 1.5
    N = 5
    t = 2
    # check if the 'model' function returns -7.5 with the previous parameters
    assert model(N,t,k) == -7.5

def test_k_float_2(): 
    """positive test that check if the 'model' function works 
    when k is a float value
    """
    #define variables for the input of 'model' function with k integer
    k = 1e3
    N = 5
    t = 2
    # check if the 'model' function returns -5e3 with the previous parameters
    assert model(N,t,k) == -5e3  
    
def test_N_positive():
    """positive test that check if the 'model' function works 
    when N is positive
    """
    #define variables for the input of 'model' function with N positive
    k = 1.5
    N = 5
    t = 2
    # check if the 'model' function returns -7.5 with the previous parameters
    assert model(N,t,k) == -7.5    

def test_k_positive(): 
    """positive test that check if the 'model' function works 
    when k is positive
    """
    #define variables for the input of 'model' function with k positive
    k = 1.5
    N = 5
    t = 2
    # check if the 'model' function returns -7.5 with the previous parameters
    assert model(N,t,k) == -7.5    

def test_TypeError_k():
    """test that check if the 'model' function raises a TypeError
    when k is not a float
    """
    #define variables for the input of 'model' function with k an array
    k = np.linspace(0,1)
    N = 5
    t = 2   
    with pytest.raises(TypeError):
         model(N,t,k)

def test_ValueError_N():
    k = 1.5
    N = -5
    t = 2   
    with pytest.raises(ValueError):
        model(N,t,k)

def test_ValueError_k():
    k = -1.5
    N = 5
    t = 2   
    with pytest.raises(ValueError):
        model(N,t,k)

def test_zero_ValueError_k():
    k = 0.0
    N = 5
    t = 2 
    with pytest.raises(ValueError):
        model(N,t,k)
        
def test_result_float(): 
    k = 1.5
    N = 5
    t = 2
    assert isinstance(model(N,t,k) , float)       
