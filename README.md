# PyPI-Package-Pi-Estimator

## Table of Contents

1. [Motivation](#motivation)
2. [About the Package](#package)
3. [Files](#files)
4. [Installation](#installation)
5. [Acknowledgements](#acknowledgements)

## Motivation <a name="motivation"></a>

This is another project of the [Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025) programm at [Udacity](https://www.udacity.com/). The aim was to create your own PyPi-Package and upload them to [pypi.org](https://pypi.org/). Due to my background, I decided to create a package on the topic of mathematics.

You can install the package with following code:
'pip install thjo-pi-estimator'

You can find more informations about how to install packages [here](https://packaging.python.org/tutorials/installing-packages/#use-pip-for-installing).

## About the Package <a name="pachake"></a>

The package provides an estimator for pi by using different approaches:

---
**Monte_Carlo_Estimator:** The simulator produces randomly n points on an area 
of 2x2 and returns the ratio of the points landed in the unit circle compared 
to those who do not.

Attributes:<br/>
number of simulation (n=100)

Methods:
1. estimate_pi(): estimation of pi given number of simulations n.<br/>
2. circle_plot(): creates a plot of the unit circle and markes the points
that landed in it. 

---
**Riemann_Sum_Estimator:** This approach approximates the integral of a quarter of the 
unit circle by Riemann sums.

Attributes:<br/>
number of Riemann sums (n=100)

Methods:
1. estimate_pi(): estimation of pi by an approximation of the integral 
with n sums.<br/>
2. circle_plot(): creates a plot of the quarter of the unit circle and 
shows the bars that represents the sums.<br/>
3. circle_plot_25(): same as method 2 but with a fixed choice of n=25. 
It shows the functionality of the model with an optimal choice of intervals.
---

## Files <a name="files"></a>

The package contains two files:
1. monte_carlo.py, class = Monte_Carlo_Estimator()
2. riemann_sum.py, class = Riemann_Sum_Estimator()

## Installation <a name="installation"></a>


## Acknowledgements <a name="acknowledgements"></a>

I would like to thank the udacity team again for the great teaching and the super Nanodegree programme.
