# Radioactive decay
Project for the exam "Software and computing for applied physics"

Master's degree in physics - curriculum: Material physics and nanoscience

University of Bologna

## Table of contents
* [Description of the project](#description-of-the-project)
* [Technologies](#technologies)
* [Files](#files)
  * [Model](#model)
  * [setn0](#setn0)
  * [setnuclei](#setnuclei)
  * [readFile](#readFile)
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
	
## Technologies
This project is created with:
* Python version: 3.8
	
## Files
The project is composed of 6 different files:
### Model
It contains the definition of the diferential equation to be solved.
### setn0
It allows you to set the initial number of nuclei $N_0$, which is the initial condition to solve the differential equation.
### setnuclei
It allows you to set the type of decaying nuclei among "Uranium238", "Plutonium239" or "Radium226". Each of them is related to a specific decay constant k.
### readFile
It reads from a text file the time values to be used in the model and puts them into an array t.
### ode
It solves the differential equation using the python function "odeint", which requires four inputs:
1. model: Function name that returns derivative values at requested y and t values as dydt = model(y,t,k);
2. y0: Initial conditions of the differential states;
3. t: Time points at which the solution should be reported;
4. args: it is a tuple sequence of values that allows additional information to be passed into the model function.
### plot
It plots the solution of the differential equation. In this case, it plots the number of nuclei N remaining after a time t.
