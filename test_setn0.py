from hypothesis import given, strategies as st
import pytest
from setn0 import verifyN0

#===========================
#PROPERTY TESTING 
#===========================

#The @given decorator 
#takes the test function and turns it 
#into a parametrized one which, when called, will run the test function 
#over a wide range of matching data from the defined strategy 'st'

#Hypothesis provides strategies 'st'
#that generate values for most built-in types 
#with arguments to constrain or adjust the output


#generate a good variables ('N0' is a positive integer)
#for the input of 'verifyN0' function and for the input of the test function
@given(N0 = st.integers(min_value = 0))
def test_good_values_h(N0):
    """positive test that check if the 'verifyN0' function 
    works when the input is a positive integer
    """
    # check that the input 'N0' is not equal to 0
    if N0 != 0:
       #check if the 'verifyN0' function returns the input value
       assert verifyN0(N0) == N0


#generate a string 'N0'
#for the input of 'verifyN0' function and for the input of the test function        
@given(N0 = st.text())
def test_TypeError_h(N0):
    """test that check if the 'verifyN0' function raises a TypeError
    when the input is not an integer, but a string
    """
    # check if the 'verifyN0' function raises a TypeError with the generated input string 'N0'
    with pytest.raises(TypeError):
        verifyN0(N0)


#generate a negative integer 'N0'
#for the input of 'verifyN0' function and for the input of the test function        
@given(N0 = st.integers(max_value = 0))
def test_ValueError_h(N0):
    """test that check if the 'verifyN0' function raises a ValueError
    when the input is a a negative integer
    """
    # check if the 'verifyN0' function raises a ValueError with the generated input 'N0'
    with pytest.raises(ValueError):
        verifyN0(N0)


#generate a value equal to 0
#for the input of 'verifyN0' function and for the input of the test function       
@given(N0 = st.just(0))
def test_zero_ValueError_h(N0):
    """test that check if the 'verifyN0' function raises a ValueError
    when the input is zero
    """
    # check if the 'verifyN0' function raises a ValueError with the generated input 'N0' 
    with pytest.raises(ValueError):
        verifyN0(N0)


#===========================
#UNIT TESTING 
#all the possible positive and negative combinations
#===========================

def test_N0_positive_integer(): 
    """positive test that check if the 'verifyN0' function works,
    returning the input value, when the input is an integer greater than 0
    """
    #define an integer greater than 0 for the input of 'verifyN0' function 
    d = 100
    #check if the 'verifyN0' function returns the input value
    assert verifyN0(d) == d

def test_TypeError():
    """test that check if the 'verifyN0' function raises a TypeError
    when the input is not an integer, but a string
    """
    #define a string variable for the input of 'verifyN0' function 
    d = '100'    
    # check if the 'verifyN0' function raises a TypeError with the defined input parameter
    with pytest.raises(TypeError):
        verifyN0(d)

def test_ValueError():
    """test that check if the 'verifyN0' function raises a ValueError
    when the input is a negative integer
    """
    #define a negative integer for the input of 'verifyN0' function 
    d = -100    
    # check if the 'verifyN0' function raises a ValueError with the defined input parameter
    with pytest.raises(ValueError):
        verifyN0(d)

def test_zero_ValueError():
    """test that check if the 'verifyN0' function raises a ValueError
    when the input is zero
    """
    #define a variable equal to 0 for the input of 'verifyN0' function 
    d = 0   
    # check if the 'verifyN0' function raises a ValueError with the defined input parameter
    with pytest.raises(ValueError):
        verifyN0(d)
