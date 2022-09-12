import numpy as np 
from readFile import verifyFile
from hypothesis import given, strategies as st
import pytest

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


#generate a good variables ('a' is a list composed of positive float elements)
#for the input of 'verifyFile' function and for the input of the test function
@given(a = st.lists(elements = st.floats(min_value=0)))
def test_good_values_h(a):
    """positive test that check if the 'verifyFile' function 
    works when the input is an array with float positive elements
    """
    # check that the list 'a' is not empty
    if a != []:
       # convert the list 'a' into a np.array 'b'
       b = np.array(a)
       # define an array 'c' composed of the sorted elements of the array 'b'
       c = np.sort(b)
       # check if the 'verifyFile' function returns the same array 'c' as in input
       assert verifyFile(b).all() == c.all()


#generate a list 'a' composed of float elements smaller than 0
#for the input of 'verifyFile' function and for the input of the test function
@given(a = st.lists(elements = st.floats(max_value=0, exclude_max = True)))
def test_ValueError_h(a):
    """test that check if the 'verifyFile' function raises a ValueError
    when the input is an array with float negative elements
    """
    # check that the list 'a' is not empty
    if a != []:
       # convert the list 'a' into a np.array 'b'
       b = np.array(a)
       # check if the 'verifyFile function raises a ValueError using the defined array 'c'
       with pytest.raises(ValueError):
          verifyFile(b)


#generate a list 'a' composed of string elements
#for the input of 'verifyFile' function and for the input of the test function
@given(a = st.lists(elements = st.text()))
def test_TypeError_h(a):
    """test that check if the 'verifyFile' function raises a TypeError
    when the input is an array with string elements
    """
    # check that the list 'a' is not empty
    if a != []:
       # convert the list 'a' into a np.array 'b'
       b = np.array(a)
       # check if the 'verifyFile function raises a TypeError using the defined array 'b'
       with pytest.raises(TypeError):
          verifyFile(b)

#generate an empty list 'a' 
#for the input of 'verifyFile' function and for the input of the test function
@given(a = st.just([]))
def test_empty_array_h(a):
    """test that check if the 'verifyFile' function raises a ValueError
    when the input array is empty
    """
    # convert the list 'a' into a np.array 'b'
    b = np.array(a)
    # check if the 'verifyFile function raises a ValueError using the defined array 'c'
    with pytest.raises(ValueError):
          verifyFile(b)

#generate a list 'a' with a NaN element
#for the input of 'verifyFile' function and for the input of the test function
@given(a = st.just(np.array([1e3,float("nan"), 1e5])))
def test_NaN_element_h(a):
    """test that check if the 'verifyFile' function raises a TypeError
    when one of the elements of the input array is not a number
    """
    # convert the list 'a' into a np.array 'b'
    b = np.array(a)
    # check if the 'verifyFile function raises a TypeError using the defined array 'b'
    with pytest.raises(TypeError):
          verifyFile(b)
          
#generate a list 'a' composed of duplicated values
#for the input of 'verifyFile' function and for the input of the test function
@given(a = st.just(np.array([1.3,1.7,1.3,1.5,1.3,1.3,1.5,1.7])))
def test_duplicated_values_h(a):
    """positive test that check if the 'verifyFile' function works 
    when one of the elements is present more than once
    """

    # convert the list 'a' into a np.array 'b'
    b = np.array(a)
    # define an array 'c' composed of the non duplicated elements of the array b
    c = np.array([1.3,1.5,1.7])
    # check if the 'verifyFile' function returns the array with non duplicated values
    assert verifyFile(b).all() == c.all()          
          
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
    """test that check if the 'verifyFile' function raises a ValueError
    when one of the elements of the input array is negative
    """
    #define the array for the input of 'verifyFile' function with one negative element
    a = np.array([1.5,-1e3,1.5e5,1e7,-1.5e11])   
    # check if the 'verifyFile' function raises a ValueError using the defined array a
    with pytest.raises(ValueError):
        verifyFile(a)

def test_TypeError():
    """test that check if the 'verifyFile' function raises a TypeError
    when one of the elements of the input array is not float
    """
    #define the array for the input of 'verifyFile' function with one string element
    a = np.array([1e3,1.5e5,1e7,'a',1.5e11])   
    # check if the 'verifyFile' function raises a TypeError using the defined array a
    with pytest.raises(TypeError):
        verifyFile(a)

def test_zero():
    """positive test that check if the 'verifyFile' function works 
    when one of the elements of the input array is zero
    """
    #define the array for the input of 'verifyFile' function with one element = 0
    a = np.array([0.,1e3,1.5e5,1e7,1.5e11])   
    # check if the 'verifyFile' function returns the same array as in input
    assert verifyFile(a).all() == a.all()
    
def test_empty_array():
    """test that check if the 'verifyFile' function raises a ValueError
    when the array is empty
    """
    #define an empty array for the input of 'verifyFile' function 
    a = np.array([])   
    # check if the 'verifyFile' function raises a ValueError using the defined array a
    with pytest.raises(ValueError):
        verifyFile(a)  
 
def test_NaN_element():
    """test that check if the 'verifyFile' function raises a TypeError
    when one of the elements of the input array is not a number
    """
    #define the array for the input of 'verifyFile' function with one NaN element
    a = np.array([1e3,float("nan"), 1e5])     
    # check if the 'verifyFile' function raises a TypeError using the defined array a
    with pytest.raises(TypeError):
        verifyFile(a)
        
def test_duplicated_values():
    """positive test that check if the 'verifyFile' function works 
    when one of the elements is present more than once
    """
    #define the array for the input of 'verifyFile' function with one element 
    #that appears more than once
    a = np.array([1.3,1.7,1.3,1.5,1.3,1.3,1.5,1.7])  
    b = np.array([1.3,1.5,1.7]) 
    # check if the 'verifyFile' function returns the array with non duplicated values
    assert verifyFile(a).all() == b.all()
