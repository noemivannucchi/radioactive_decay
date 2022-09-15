# Radioactive decay
Project for the exam "Software and computing for applied physics"

Master's degree in physics - curriculum: Material physics and nanoscience

University of Bologna

## Table of contents
* [Description of the project](#description-of-the-project)
* [Usage](#usage)
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
  * [fit and fit_funct](#fit_and_fit_funct)
  * [configfit.ini](#configfit.ini)
  * [par_from_fit.txt](#par_from_fit.txt)
  * [compare_params and test_compareparams](#compare_params_and_test_compareparams)
  * [inter_extra_polation](#inter_extra_polation)
  * [configx.ini](#configx.ini)
  * [inter_extra_function and test_polation](#inter_extra_function_and_test_polation)
  
## Description of the project
This project aims to solve an ordinary differential equation (ODE) describing the radioactive decay of N nuclei after a time t. 
If there are N(t) radioactive nuclei at time t and $N_0$ at t = 0, and if their rate of decay (-dN/dt) is proportional to the number of undecayed nuclei N, with constant of proportionality k (in $s^{-1}$), then
$$\frac{dN}{dt} = -k N $$
and integrating it, it is possible to obtain:

$$ N = N_0 e^{-kt} $$

Therefore, the initial number of radioactive nuclei decays exponentially.

After setting the initial conditions, the decay constant and the array containing the time values, integration is performed and the curve of the number of nuclei N remaining after a time t (in s) is plotted.
The figure below shows an example of exponential radioactive decay in the case of the nucleus Radium226, using the time values in the file "times.txt".

![example_plot_decay](https://user-images.githubusercontent.com/79851600/187657314-e6d6c336-b33a-4131-9278-3d244e72e8f5.png)

After that, it is possible to perform a fit of the previous curve with a decreasing exponential function and plot the fitting curve on the initial data, like in the figure below. Then, it is determined the quality of the fit by calculating R squared, the parameters are extracted with their standard deviation and they are compared to the initial expected parameters.

![fit_exp_decay](https://user-images.githubusercontent.com/79851600/190357530-881384d9-ed6c-4d7f-add5-c1cdcd0ab19a.png)

Finally, the parameters extracted from the fit are used to do an interpolation or extrapolation of new data. This can be done by setting the new value to interpolate or extrapolate in a configuration file.

## Usage
To solve the ODE you have to:
* set in the configuration file 'config.ini' the initial number of radioactive nuclei, the type of nuclei and the name of the text file with the time values
* execute the file 'ode' 

To plot the solutions of the differential equations (number of remaining nuclei after a time t vs t):
* execute the file 'plot' 

To do the exponential fit you have to:
* set in the configuration file 'configfit.ini' the initial parameters (the initial number of nuclei N0, the decay constant k related to the chosen nuclei and a constant b) for the fitting function y = N0 * np.exp(-k * x) + b 
* execute the file 'fit'

To do the intepolation/extrapolation you have to:
* set in the configuration file 'configx.ini' the 'x' value of the fitting function y = N0 * exp(-k * x) + b in order to make an interpolation or extrapolation of the corresponding y value.
* execute the file 'inter_extra_polation'

To run the tests (property and unit) it is mandatory to have installed the package 'pytest' and you have to write on the command line:
```python
 !pytest nametest.py
```

For example, in the case of the test file 'test_readFile', the command is:
```python
 !pytest test_readFile.py
```

This command will execute all the functions that begin with 'test' and it will show if the tests pass or not.

## Technologies
This project is created with:
* Python version: 3.8

The following libraries and packages are required:
* Hypothesis
* Pytest
* Numpy
* scipy.integrate
* scipy.optimize
* matplotlib.pyplot
* ConfigParser
	
## Files
The project is composed of 23 different files:
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
The function in the file 'readFile' checks that the input array with the time values (in s) is not empty and it removes the duplicated elements. Then, it checks that the elements are positive float numbers and returns the array with sorted values. On the other hand, if the elements are not numbers or positive or float, it raises an error.
The 'test_readFile' file contains all the tests (unit and property tests) related to the function in the file 'readFile'.
### times.txt
It is just an example of some time values in the case of "Radium226". It can be used to run 'odeint' and 'plt.plot' functions.
### ode
It solves the differential equation using the scipy.integrate function "odeint", which requires four inputs:
1. model: Function name that returns derivative values at requested y and t values as dydt = model(y,t,k);
2. y0: Initial conditions of the differential states;
3. t: Time points at which the solution should be reported; 
4. args: it is a tuple sequence of values that allows additional information to be passed into the model function.

In this file, the initial condition $N_0$ to solve ODE, the type of nuclei and the name of the text file with time values, which will be converted into an array, are taken from the configuration file 'config.ini'.
Finally the ODE are solved by the function 'odeint' and the results are saved in the file 'results.txt'.
### config.ini
This configuration file allows you to set:
* the type of nuclei among "Uranium238", "Plutonium239" or "Radium226"
* the initial number of nuclei N0
* the name of a text file with time values

It is used for the input of 'odeint' function to solve ODE. As an example, it contains the values for "Radium226" case.
### results.txt
This text file contains the results of the 'odeint' function and it is loaded in the 'plot' file to plot the solutions.
### plot
It loads the results of the ODE from the file 'results.txt' and it plots the solution of the differential equation. In this case, it plots the number of radioacive decaying nuclei N remaining after a time t vs time t (in s).
You can also set x and y labels and put the grid.
### fit and fit_funct
It loads the time values and the corresponding resulting values from 'odeint'. Then it fits these points with the function 'fitfunct', which represents a decreasing exponential function 'y = N0 * np.exp(-k * x) + b' and whose definition can be found in the file 'fit_funct'. The initial expected parameters for the fitting function are taken from the configuration file 'configfit.ini'. In addition, it plots the fit curve on the initial data and it prints R squared and the parameters extracted from the fit with their standard deviations. Finally, it checks that the parameters extracted from the fit are coherent with the expected ones within the uncertainty range given by their standard deviation, by using the function defined in the file 'compare_params'.
### configfit.ini
This configuration file allows you to set the initial parameters for the fitting function 'fitfunct':
* N0 which is the initial number of nuclei
* k which is the decay constant (in s^-1) related to the chosen nuclei
* b which is a constant that has to be close to 0 in this model

As an example, it contains the values near those we expect for "Radium226".
### par_from_fit.txt
This text file contains the parameters (N0, k, b) extracted from the fit and it is loaded in the 'inter_extra_polation' file to to an interpolation or extrapolation of some new data. 
### compare_params and test_compareparams
This function checks that the parameters extracted from the fit are consistent with those expected within the uncertainty given by the standard deviation. If the expected parameters are within the uncertainty range of the extracted ones, it is printed that the extracted parameters are coherent with the expected ones. Otherwise, it is printed that more points are needed to better estimate the parameters N0, k, b.
The 'test_compareparams' file contains all the tests related to the function in the file 'compare_params'.
### inter_extra_polation
This file loads the parameters extracted from the fit to do an interpolation or extrapolation in order to extract the number of remaining nuclei at a new time x. The configuration file 'configfit.ini' allows to set the new value x to interpolate or extrapolate. Then, the calculation is performed by the function contained in the 'inter_extra_function' file.
### configx.ini
This configuration file allows you to set the 'x' value of the fitting function y = N0 * exp(-k * x) + b in order to make an interpolation or extrapolation of the corresponding y value. x represents a time value (in s), while N0, k, b are the parameters extracted from the fit. As an example, this file contains a time value for extrapolation in the case of "Radium226".
### inter_extra_function and test_polation
This function calculate the number of remaining nuclei N at the selected time x. It is based on an interpolation/extrapolation from the fitting function N0 * np.exp(-k * x) + b, using the parameters extracted from the fit N0, k, b. In particular, it checks if the input time 'x' is whitin the minimum and the maximum time values, thus distinguishing the case of interpolation and extrapolation, and returns a dictionary 'd' containing the number of remaining nuclei N at the selected time x.
The 'test_polation' file contains all the tests related to the function in the file 'inter_extra_function'.
