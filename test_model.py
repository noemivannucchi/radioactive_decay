from model import model
from hypothesis import given, strategies as st
import pytest
import numpy as np

def test_k_float(): #positive test
    k = 1.5
    N = 5
    t = 2
    assert model(N,t,k) == -7.5

def test_k_float_2(): #positive test
    k = 1e3
    N = 5
    t = 2
    assert model(N,t,k) == -5e3  
    
def test_N_positive(): #positive test
    k = 1.5
    N = 5
    t = 2
    assert model(N,t,k) == -7.5    

def test_k_positive(): #positive test
    k = 1.5
    N = 5
    t = 2
    assert model(N,t,k) == -7.5    

def test_TypeError_k():
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
