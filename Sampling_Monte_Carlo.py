
# coding: utf-8

# # Sampling using Monte Carlo
# 
# Change the parameters below to generate new results
# 

# In[ ]:


# Using numpy to support math operations with random numbers

import numpy as np

# csv module to export results

import csv


# In[ ]:


# CHANGE PARAMETERS HERE!

# min sample_size, max_sample_size => Maximum Sample Size to be simulated
min_sample_size = 100
max_sample_size = 1000

# p => Event Probability
p = 0.005

# e => Error rate
e = 0.01

# s => Number of simulations. Anything more than 10000 simulations won't
#      change responses quite much
s = 10000


# In[ ]:


# Functions to generate sample simulations

def sim_generator(sample_size):
  results = np.zeros(s) # generate an empty array to be populated with results
  
  for it in np.arange(0,s):  # Iterate over number of simulations
    arr = np.random.binomial(1,p,sample_size) # Simulate event on sample size
    num = np.count_nonzero(arr) # count the number of successes
    num_adjusted = np.random.binomial(1,1-e,num) # adjust for the error rate
    num_count = np.count_nonzero(num_adjusted) # count adjusted events
    response = float(num_count >= 1) # convert responses to final array
    results[it] = response # populate responses in final array
  
  return np.count_nonzero(results) / s 
  # Return % of simulations in which we have at least one success, 
  # given the sample_size
  

def sim_multiple_samples(min_size,max_size):
  """
  This function simulates multiple samples, generating a dictionary.
  In the left hand
  """
  sim_results = {}
  
  for i in np.arange(min_size,max_size+1):
    sim_results[str(i)] = sim_generator(i)
    
  return sim_results


# In[ ]:


# Running the model

sample_prob = sim_multiple_samples(min_sample_size,max_sample_size)


# In[ ]:


# Generating CSV to export

with open('final_results.csv', 'w') as f:
    f.write('sample_size,prob_at_least_one_pct\n')
    for key in sample_prob.keys():
        f.write("%s,%s\n"%(key,sample_prob[key]))


# In[220]:


# Checking results:
print("Number of simulations:",s,"\n")

for key in sample_prob.keys():
  print("Sample size:",key," --> Probability of having at least 01 success:",sample_prob[key])

