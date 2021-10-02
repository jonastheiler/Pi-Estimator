import numpy as np
import matplotlib.pyplot as plt

class Leibniz_Series_Estimator():
    """
    This estimator creates a finite, alternating series to approsimate pi.
    
    """
    
    def __init__(self, n=100):
        
        self.n = n
        
        
    def estimate_pi(self):
        """
        Function to estimate pi by a finite, alternating sum.

        """
        
        # estimate pi with leibniz serie
        pi_est = 4*sum((-1)**i/(2*i + 1) for i in range(self.n))
        
        error = round(100*abs(pi_est - np.pi)/np.pi,6)
        
        return 'estimation of pi: {}, error: {}%'.format(pi_est, error)
    
    
    def series_plot(self):
        """
        Function to plot the series by the number of iterations.

        """
        
        fig, ax = plt.subplots(1)
        
        # for loop to create bar plots
        for x in range(self.n+1):
            ax.bar(x-1, 4*sum((-1)**i/(2*i + 1) for i in range(x)),
                   width=0.5,
                   alpha=0.2,
                   align='edge',
                   edgecolor='b')
        
        # create red line to indicate pi
        ax.axhline(y=np.pi, color='r').set_linewidth(0.5)

        plt.xlim(-0.25,self.n + 1)
        plt.ylim(-0.25,4.25)
        
        plt.grid(linestyle='--')

        plt.title('Leibniz Series converting to pi', fontsize=8)
        
        plt.show()