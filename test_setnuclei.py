from hypothesis import given, strategies as st
import pytest
from setnuclei import verifynuclei

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


#generate a string equal to 'Uranium238'
#for the input of 'verifynuclei' function and for the input of the test function
@given(d = st.just('Uranium238'))
def test_k_uranium_h(d):
    """positive test that check if the 'verifynuclei' function 
    returns the right decay constant 'k' (k = 5e-18)
    when the input is 'Uranium238'
    """
    # check if the 'verifynuclei' function returns 5e-18 with the generated input string 'd'
    assert verifynuclei(d) == 5e-18
    

#generate a string equal to 'Plutonium239'
#for the input of 'verifynuclei' function and for the input of the test function    
@given(d = st.just('Plutonium239'))
def test_k_plutonium_h(d):
    """positive test that check if the 'verifynuclei' function 
    returns the right decay constant 'k' (k = 9e-13)
    when the input is 'Plutonium239'
    """
    # check if the 'verifynuclei' function returns 9e-13 with the generated input string 'd'
    assert verifynuclei(d) == 9e-13


#generate a string equal to 'Radium226'
#for the input of 'verifynuclei' function and for the input of the test function    
@given(d = st.just('Radium226'))
def test_k_radium_h(d):
    """positive test that check if the 'verifynuclei' function 
    returns the right decay constant 'k' (k = 1e-11)
    when the input is 'Radium226'
    """
    # check if the 'verifynuclei' function returns 1e-11 with the generated input string 'd'
    assert verifynuclei(d) == 1e-11


#generate a string 'd'
#for the input of 'verifynuclei' function and for the input of the test function   
@given(d = st.characters())
def test_ValueError_h(d):
    """test that check if the 'verifynuclei' function raises a ValueError
    when the input string is not one of the allowed string values
    """
    #check that the input string 'd' is not equal to one of the allowed nuclei
    if d !='Uranium238' and d !='Plutonium239' and d !='Radium226':
     # check if the 'verifynuclei' function raises a ValueError with the generated input string 'd'
     with pytest.raises(ValueError):
        verifynuclei(d)


#generate a fraction 'd'
#for the input of 'verifynuclei' function and for the input of the test function        
@given(d = st.fractions())
def test_TypeError_h(d):
    """test that check if the 'verifynuclei' function raises a TypeError
    when the input is not a string, but a fraction
    """
    # check if the 'verifynuclei' function raises a TypeError with the generated input fraction 'd'
    with pytest.raises(TypeError):
        verifynuclei(d)     


#generate a string equal to 'Uranium238'
#for the input of 'verifynuclei' function and for the input of the test function        
@given(d = st.just('Uranium238'))
def test_result_float_h(d):
    """positive test that check if the 'verifynuclei' function 
    returns a float value
    when the input is 'Uranium238'
    """
    # check if the 'verifynuclei' function returns a float value with the generated input string 'd'
    assert isinstance(verifynuclei(d) , float)  


#===========================
#UNIT TESTING 
#all the possible positive and negative combinations
#===========================

def test_k_uranium():
    """positive test that check if the 'verifynuclei' function 
    returns the right decay constant 'k' (k = 5e-18)
    when the input is 'Uranium238'
    """
    #define the variable for the input of 'verifynuclei' function 
    d = 'Uranium238'
    # check if the 'verifynuclei' function returns 5e-18 with the defined input parameter
    assert verifynuclei(d) == 5e-18

def test_k_plutonium():
    """positive test that check if the 'verifynuclei' function 
    returns the right decay constant 'k' (k = 9e-13)
    when the input is 'Plutonium239'
    """
    #define the variable for the input of 'verifynuclei' function 
    d = 'Plutonium239'
    # check if the 'verifynuclei' function returns 9e-13 with the defined input parameter
    assert verifynuclei(d) == 9e-13
    
def test_k_radium():
    """positive test that check if the 'verifynuclei' function 
    returns the right decay constant 'k' (k = 1e-11)
    when the input is 'Radium226'
    """
    #define the variable for the input of 'verifynuclei' function 
    d = 'Radium226'
    # check if the 'verifynuclei' function returns 1e-11 with the defined input parameter
    assert verifynuclei(d) == 1e-11
    
def test_ValueError():
    """test that check if the 'verifynuclei' function raises a ValueError
    when the input string is not one of the allowed string values
    """
    #define a string variable for the input of 'verifynuclei' function 
    #the value of the defined string 'd' is not one of the allowed nuclei
    d = 'Uranium200'   
    # check if the 'verifynuclei' function raises a ValueError with the defined input parameter
    with pytest.raises(ValueError):
        verifynuclei(d)
        
def test_TypeError():
    """test that check if the 'verifynuclei' function raises a TypeError
    when the input is not a string, but an integer
    """
    #define an integer variable for the input of 'verifynuclei' function 
    d = 100  
    # check if the 'verifynuclei' function raises a TypeError with the defined input parameter
    with pytest.raises(TypeError):
        verifynuclei(d)        
        
def test_result_float(): 
    """positive test that check if the 'verifynuclei' function 
    returns a float value
    when the input is 'Radium226'
    """
    #define the variable for the input of 'verifynuclei' function
    d = 'Radium226'
    # check if the 'verifynuclei' function returns a float value with the defined input parameter
    assert isinstance(verifynuclei(d) , float)        
