# PyPI-Package-Pi-Estimator

## Table of Contents

1. [Motivation](#motivation)
2. [About the Package](#package)
3. [Files](#files)

## Motivation <a name="motivation"></a>
This packages provides three different approaches to approximate the number pi. Each approach contains a plot method to visualise what is happening. The package has been uploaded to [PyPI](https://pypi.org/project/thjo-pi-estimator/) and was created in Python.

You can install the package with following code:<br/>
`pip install thjo-pi-estimator`

If you want to use for example the *"Riemann_Sum_Estimator"* you need the 
following code:<br/>
`from thjo_pi_estimator import Riemann_Sum_Estimator`

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
shows the bars that represents the sums.
---

**Leibniz_Series_Estimator:** This approach builds a finite, alternating 
Leibniz series to approximate pi.

Attributes:<br/>
number of summands (n=100)

Methods:
1. estimate_pi(): estimation of pi by a finite, alternating Leibniz series.<br/>
2. series_plot(): creates a barplot of the summands and indicates the 
convergence to pi.
---

## Files <a name="files"></a>

The package contains two files:
1. monte_carlo.py, class = Monte_Carlo_Estimator()
2. riemann_sum.py, class = Riemann_Sum_Estimator()
3. leibniz_series.py, class = Leibniz_Series_Estimator()
