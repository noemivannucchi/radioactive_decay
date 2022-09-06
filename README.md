# Radioactive decay
Project for the exam "Software and computing for applied physics"

Master's degree in physics - curriculum: Material physics and nanoscience

University of Bologna

## Table of contents
* [Description of the project](#description-of-the-project)
* [Technologies](#technologies)
* [Files](#files)
  * [Model and test_model](#model)
  * [setn0 and test_setn0](#setn0)
  * [setnuclei and test_setnuclei](#setnuclei)
  * [readFile and test_readFile](#readFile)
  * [times.txt](#times.txt)
  * [ode](#ode)
  * [plot](#plot)

## Description of the project
This project aims to solve an ordinary differential equation describing the radioactive decay of N nuclei after a time t. 
If there are N(t) radioactive nuclei at time t and $N_0$ at t = 0, and if their rate of decay (-dN/dt) is proportional to the number of undecayed nuclei N, with constant of proportionality k, then
$$\frac{dN}{dt} = -k N $$
and integrating it, it is possible to obtain:

$$ N = N_0 e^{-kt} $$

Therefore, the initial number of radioactive nuclei decays exponentially.

After setting the initial conditions, the decay constant and entering the array containing the time values, integration is performed and the graph of the number of nuclei N remaining after a time t is plotted.
The figure below shows an example of exponential radioactive decay in the case of Radium226, using the time values in the file "times.txt".

![example_plot_decay](https://user-images.githubusercontent.com/79851600/187657314-e6d6c336-b33a-4131-9278-3d244e72e8f5.png)

## Technologies
This project is created with:
* Python version: 3.8
	
## Files
The project is composed of 7 different files:
### Model and test_model
It contains the definition of the diferential equation to be solved.
### setn0 and test_setn0
It allows you to set the initial number of nuclei $N_0$, which is the initial condition to solve the differential equation.
### setnuclei and test_setnuclei
It allows you to set the type of decaying nuclei among "Uranium238", "Plutonium239" or "Radium226". Each of them is related to a specific decay constant k.
### readFile and test_readFile
It reads from a text file the time values to be used in the model and puts them into an array t.
### times.txt
It is just an example of some time values in the case of "Radium226". It can be used to run 'readFile' and 'odeint' functions.
### ode
It solves the differential equation using the python function "odeint", which requires four inputs:
1. model: Function name that returns derivative values at requested y and t values as dydt = model(y,t,k);
2. y0: Initial conditions of the differential states;
3. t: Time points at which the solution should be reported;
4. args: it is a tuple sequence of values that allows additional information to be passed into the model function.
### plot
It plots the solution of the differential equation. In this case, it plots the number of nuclei N remaining after a time t.

## Usage
