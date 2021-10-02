# PyPI-Package-Pi-Estimator

## Table of Contents

1. [Motivation](#motivation)
2. [About the Package](#package)
3. [Files](#files)

## Motivation <a name="motivation"></a>
This packages provides three different approaches to estimate and approximate the number pi. Each approach contains a plot method to visualise what is happening. The package has been uploaded to test.pypi.org and was created in Python. I created this package in order to sharpen my **Object-Oriented-Programming** skills.


## About the Package <a name="pachake"></a>

The package provides an estimator for pi by using different approaches:
---
**Monte_Carlo_Estimator:** This estimator generates random points in a 2x2 area and calculates the ratio of points that end up inside the unit circle. Since we know that the area of the unit circle is equal to Pi, we can multiply this ratio by 4 (total area).

Attributes:<br/>
number of simulation (n=1000)

Methods:
1. estimate_pi(): function to estimate pi given n uniformly distributed points on a area 2X2.<br/>
2. circle_plot(): function to plot the unit circle and the simulated points. 

---
**Riemann_Sum_Approximation:** Although this approach differs from Monte Carlo, it has one thing in common: here, too, we try to approximate the area of the unit circle (which, as we know, is pi). To achieve this, we try to approximate the integral of the function sqrt(1-x²) from 0 to 1 and multiply by 4.

Attributes:<br/>
number of Riemann sums (n=100)

Methods:
1. approximate_pi(): function to approximate the integral of a quarter of the unit circle.<br/>
2. bar_plot(): function to plot a quarter of the unit circle and the approximation with n intervals.
---

**Leibniz_Series_Approximation:** This approach works completely differently from the others. The Leibniz formula for pi, named after Gottfried Leibniz, already provides what we are looking for. So in this approach, the first n summands are taken and multiplied by 4.

Attributes:<br/>
number of summands (n=100)

Methods:
1. approximate_pi(): function to approximate pi by a finite, alternating sum.<br/>
2. series_plot(): function to plot the series by the number of iterations.
---

## Files <a name="files"></a>

The package contains two files:
1. monte_carlo.py, class = Monte_Carlo_Estimator()
2. riemann_sum.py, class = Riemann_Sum_Estimator()
3. leibniz_series.py, class = Leibniz_Series_Estimator()
