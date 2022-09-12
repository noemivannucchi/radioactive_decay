# Radioactive decay
Project for the exam "Software and computing for applied physics"

Master's degree in physics - curriculum: Material physics and nanoscience

University of Bologna

## Table of contents
* [Usage](#usage)
* [Description of the project](#description-of-the-project)
* [Technologies](#technologies)
* [Files](#files)
  * [Model and test_model](#Model_and_test_model)
  * [setn0 and test_setn0](#setn0_and_test_setn0)
  * [setnuclei and test_setnuclei](#setnuclei_and_test_setnuclei)
  * [readFile and test_readFile](#readFile_and_test_readFile)
  * [times.txt](#times.txt)
  * [ode](#ode)
  * [config.ini](#config.ini)
  * [results.txt](#results.txt)
  * [plot](#plot)

## Usage
To run this program you have to:
* set in the configuration file 'config.ini' the initial number of radioactive nuclei, the type of nuclei and the name of the text file with the time values
* execute the file 'ode' in order to solve the differential equations
* execute the file 'plot' to plot the solutions of the differential equations (number of remaining nuclei after a time t vs t)


To run the tests (property and unit) it is mandatory to have installed the package 'pytest' and you have to write on the command line:
```python
 !pytest nametest.py
```

For example, in the case of the test file 'test_readFile', the command is:
```python
 !pytest test_readFile.py
```

This command will execute all the functions that begin with 'test' and it will show if the tests pass or not.

## Description of the project
This project aims to solve an ordinary differential equation (ODE) describing the radioactive decay of N nuclei after a time t. 
If there are N(t) radioactive nuclei at time t and $N_0$ at t = 0, and if their rate of decay (-dN/dt) is proportional to the number of undecayed nuclei N, with constant of proportionality k (in $s^{-1}$), then
$$\frac{dN}{dt} = -k N $$
and integrating it, it is possible to obtain:

$$ N = N_0 e^{-kt} $$

Therefore, the initial number of radioactive nuclei decays exponentially.

After setting the initial conditions, the decay constant and entering the array containing the time values, integration is performed and the graph of the number of nuclei N remaining after a time t (in s) is plotted.
The figure below shows an example of exponential radioactive decay in the case of the nucleus Radium226, using the time values in the file "times.txt".

![example_plot_decay](https://user-images.githubusercontent.com/79851600/187657314-e6d6c336-b33a-4131-9278-3d244e72e8f5.png)

## Technologies
This project is created with:
* Python version: 3.8

The following libraries and packages are required:
* Hypothesis
* Pytest
* Numpy
* scipy.integrate
* matplotlib.pyplot
* ConfigParser
	
## Files
The project is composed of 13 different files:
### Model and test_model
It contains the definition of the diferential equation to be solved. This model represents the exponential decay of one type of radioactive nuclei in time with a decay constant k (in $s^{-1}$). In the 'model' function, it is verified that k is a float value greater than 0 and N is positive, otherwise it raises an error.
The 'test_model' file contains all the tests (unit and property tests) related to the 'model' function.
### setn0 and test_setn0
These files concern the initial number of radioactive nuclei $N_0$, which is the initial condition to solve the differential equation.
The function in the file 'setn0' checks that the input value $N_0$ is an integer greater than 0, otherwise it raises an error.
The 'test_setn0' file contains all the tests (unit and property tests) related to the function in the file 'setn0'.
### setnuclei and test_setnuclei
These files regard the type of decaying nuclei. This program allows only three choices of radioactive nuclei: "Uranium238", "Plutonium239" or "Radium226". Each of them is related to a specific decay constant k (in $s^{-1}$).
The function in the file 'setnuclei' checks that the input value is a string and it corresponds to one of the allowed types of radioactive nuclei contained in the dictionary, otherwise it raises an error. Then it sets the relative float decay constant k.
The 'test_setnuclei' file contains all the tests (unit and property tests) related to the function in the file 'setnuclei'.
### readFile and test_readFile
These files regard the array containing the time values (in s) to be used in the 'model' function and for the integration of the differential equation.
The function in the file 'readFile' checks that the input array with the time values (in s) is not empty and it removes the duplicated elements. Then it checks that the elements are positive float numbers and returns the array with sorted values. On the other hand, if the elements are not numbers or positive or float, it raises an error.
The 'test_readFile' file contains all the tests (unit and property tests) related to the function in the file 'readFile'.
### times.txt
It is just an example of some time values in the case of "Radium226". It can be used to run 'odeint' and 'plt.plot' functions.
### ode
It solves the differential equation using the scipy.integrate function "odeint", which requires four inputs:
1. model: Function name that returns derivative values at requested y and t values as dydt = model(y,t,k);
2. y0: Initial conditions of the differential states;
3. t: Time points at which the solution should be reported; 
4. args: it is a tuple sequence of values that allows additional information to be passed into the model function.

In this file, the initial condition $N_0$ to solve ODE, the type of nuclei and the name of the text file with time values, which will be converted into an array, are taken from the configuration file.
Finally the ODE are solved by the function 'odeint' and the results are saved in the file 'results.txt'.
### config.ini
This configuration file allows you to set:
* the type of nuclei among "Uranium238", "Plutonium239" or "Radium226"
* the initial number of nuclei N0
* the name of a text file with time values
### results.txt
This text file contains the results of the 'odeint' function and it is loaded in the 'plot' file to plot the solutions
### plot
It loads the results of the ODE from the file 'results.txt' and it plots the solution of the differential equation. In this case, it plots the number of radioacive decaying nuclei N remaining after a time t vs time t (in s).
You can also set x and y labels and put the grid.
