import numpy as np 
from readFile import verifyFile
from hypothesis import given, strategies as st
import pytest

#===========================
#PROPERTY TESTING 
#===========================
@given(a = st.lists(elements = st.floats(min_value=0)))
def test_good_values_h(a):
    if a != []:
       b = np.array(a)
       c = np.sort(b)
       assert verifyFile(c).all() == c.all()

@given(a = st.lists(elements = st.floats(max_value=0, exclude_max = True)))
def test_ValueError_h(a):
    if a != []:
       with pytest.raises(ValueError):
          verifyFile(a)

@given(a = st.lists(elements = st.text()))
def test_TypeError_h(a):
    if a != []:
       with pytest.raises(TypeError):
          verifyFile(a)

#===========================
#UNIT TESTING 
#all the possible positive and negative combinations
#===========================

def test_elements_float():
    """positive test that check if the 'verifyFile' function works 
    when the input is an array with floats elements
    """
    #define the array for the input of 'verifyFile' function with floats elements
    a = np.array([1.5,1e3,1.5e5,1e7,1.5e11]) 
    # check if the 'verifyFile' function returns the same array as in input
    assert verifyFile(a).all() == a.all()

def test_sorting_elements():
    """positive test that check if the 'verifyFile' function
    correctly sorts the elements of the input array
    """
    #define the array for the input of 'verifyFile' function with unsorted elements
    a = np.array([1.5e5,1e7,1e3,1.5e11,1.5])    
    #define an other array with sorted elements from the previous array
    sorteda = np.array([1.5,1.5e3,1.5e5,1.5e7,1.5e11])
    #check if the elements in the output array of the 'verifyFile' function
    #are equal to the elements in the sorted array 'sorteda'
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
