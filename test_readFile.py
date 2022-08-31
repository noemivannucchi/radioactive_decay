import numpy as np 
from readFile import verifyFile
from hypothesis import given, strategies as st
import pytest

def test_elements_float(): #positive test
    a = np.array([1.5,1e3,1.5e5,1e7,1.5e11]) 
    assert verifyFile(a).all() == a.all()

def test_sorting_elements():
    a = np.array([1.5e5,1e7,1e3,1.5e11,1.5])     
    sorteda = np.array([1.5,1.5e3,1.5e5,1.5e7,1.5e11])
    assert verifyFile(a).all() == sorteda.all()

def test_ValueError():
    a = np.array([-1.5,1e3,1.5e5,1e7,1.5e11])   
    with pytest.raises(ValueError):
        verifyFile(a)

def test_TypeError():
    a = np.array(['a',1e3,1.5e5,1e7,1.5e11])   
    with pytest.raises(TypeError):
        verifyFile(a)

def test_zero():
    a = np.array([0,1e3,1.5e5,1e7,1.5e11])   
    assert verifyFile(a).all() == a.all()