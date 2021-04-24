#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[5]:


poisson_output = pandas.read_csv('poisson_output.csv')


# In[33]:


ca_series = poisson_output.iloc[:,1:77].idxmax(axis=1).str.split("_",expand=True).iloc[:,3]
hr_series = poisson_output.iloc[:,78:100].idxmax(axis=1).str.split("_",expand=True).iloc[:,1]
covid_diff_series = poisson_output['rev_post']-poisson_output['rev_pre']
total_revenue_series = poisson_output['rev_post']
tip_series = poisson_output['tip_per_trip']


# In[41]:


frame = pandas.DataFrame({'Community Area': ca_series,
                     'Hour':hr_series,
                     'Covid Diff':covid_diff_series,
                     'Total Revenue': total_revenue_series,
                     'Tip per Trip': tip_series})
frame.to_csv('viz_input.csv')
 

