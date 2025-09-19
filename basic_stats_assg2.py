"""**Sample Standard Deviation**

**Steps**  
We will use t-distribution because  
The sample size is small (typically n<30)  
Population Standard Deviation (sigma) is unknown   
Here we have   
n=15  
CI=0.99  
alpha=0.01 and alpha/2=0.005   
t_critical=stats.t.ppf()  
upper and lower CI=sample_mean +- t_critical*(sample_stdev/np.sqrt(n))
"""

import numpy as np
import scipy.stats as stats

sample_data=[1.13, 1.55, 1.43, 0.92, 1.25, 1.36, 1.32, 0.85, 1.07, 1.48, 1.20, 1.33, 1.18, 1.22, 1.29]

sample_mean=np.mean(sample_data)
print(sample_mean)

sample_stdev=np.std(sample_data,ddof=1)
print(sample_stdev)

t_critical=stats.t.ppf(0.995,14)
print(t_critical)

upper_ci=sample_mean+t_critical*(sample_stdev/np.sqrt(15))
print(upper_ci)

lower_ci=sample_mean-t_critical*(sample_stdev/np.sqrt(15))
print(lower_ci)

"""**Population Standard Deviation**

**Steps**  
We will use z-distribution because  
Population Standard Deviation (sigma) is known   
sigma=0.2   
z_critical=stats.norm.ppf()  
upper and lower CI=sample_mean +- z_critical*(sigma/np.sqrt(n))
"""

sigma = 0.2

z_critical=stats.norm.ppf(0.995)
print(z_critical)

upper_ci=sample_mean+z_critical*(sigma/np.sqrt(15))
print(upper_ci)

lower_ci=sample_mean-z_critical*(sigma/np.sqrt(15))
print(lower_ci)
