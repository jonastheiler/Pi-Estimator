import math
import numpy as np
import matplotlib.pyplot as plt

class Riemann_Sum_Estimator():
    """
    This estimator creates an approximation the integral of the quarter circle
    by a finite (=n) sum. To estimate pi, this approximation will be
    multiplicated with the number 4.
    
    """
    
    def __init__(self, n=100):
        
        self.n = n
    
    
    def estimate_pi(self):
        """
        Function to estimate pi by an approximation of the integral of the a 
        quarter of the unit circle.
        
        """
        
        d = 1/self.n
        
        # function to estimate pi by summing the areas of the bars
        pi_est = 4*d*sum(math.sqrt(1 - x**2) for x in np.linspace(0,1,self.n + 1))
        error = round(100*abs(pi_est - np.pi)/np.pi,6)
        
        return 'estimation of pi: {}, error: {}%'.format(pi_est, error)
            
        
    def circle_plot(self):
        """
        Function to plot a quarter of the unit circle and the approximation
        with n intervals.

        """
        
        d = 1/self.n
        
        seq = np.linspace(0, 0.5*np.pi, 25)

        u = np.cos(seq)
        v = np.sin(seq)
        
        fig, ax = plt.subplots(1)
        
        # for loop to create the bar plots
        for x in np.linspace(0,1,self.n + 1):
            ax.bar(x, math.sqrt(1 - x**2),
                   width=d,
                   alpha=0.2,
                   align='edge',
                   edgecolor='b')

        ax.plot(u, v)

        ax.set_aspect(1)

        plt.xlim(-0.25,1.25)
        plt.ylim(-0.25,1.25)

        plt.grid(linestyle='--')

        plt.title('plot unit circle for pi estimation', fontsize=8)
        
        plt.show()