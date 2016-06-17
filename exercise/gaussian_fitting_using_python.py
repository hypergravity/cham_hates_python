
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[2]:

from astroML.stats import binned_statistic

# generate data
xdata = np.random.randn(1000)
# set bins
bins=np.arange(-5., 5., .5)
# bin data
n,bin_edges = binned_statistic(xdata,xdata,statistic='count',bins=bins)
# convert bin_edge to bin_center
xpos = bins[:-1]+0.25


# In[3]:

xpos, n


# # If you don't care about the confidence interval of parameter

# In[5]:

from lmfit.models import GaussianModel
# initialize the gaussian model
gm = GaussianModel()
# take a look at the parameter names
print gm.param_names
# I get RuntimeError since my numpy version is a little old


# In[6]:

# guess parameters
par_guess = gm.guess(n,x=xpos)
# fit data
result = gm.fit(n, par_guess, x=xpos, method='leastsq')
# quick look at result
print result.fit_report()


# In[7]:

# get best fit error and stderr
print result.params['amplitude'].value,result.params['amplitude'].stderr
print result.params['center'].value,result.params['center'].stderr
print result.params['sigma'].value,result.params['sigma'].stderr


# In[8]:

fig = plt.figure()
plt.hist(xdata, bins=bins)
plt.plot(xpos, result.best_fit, 'green')


# # If you want the confidence intervals 

# In[9]:

import lmfit
def my_gaussian_model(p, x, y):
    a = np.float(p['a'])
    b = np.float(p['b'])
    c = np.float(p['c'])
    return a/np.sqrt(2.*c) * np.exp( -np.power(x-b,2.)/2./np.power(c, 2.)) - y
pars = lmfit.Parameters()
pars.add_many(('a',0.1), ('b',0.1), ('c',0.1))


# In[10]:

# initialize the minimizer
mini = lmfit.Minimizer(my_gaussian_model, pars, (xpos, n))

# do the minimization
result = mini.minimize(method='leastsq')

# print the fit report
print lmfit.fit_report(mini.params)

# NOTE
# the parameter 'a' in function my_gaussian_model is different from the built-in model in lmfit
# so the amplitude value is a little different


# In[11]:

# predit the confidence interval of all parameters
ci, trace = lmfit.conf_interval(mini, sigmas=[0.68,0.95],
                                trace=True, verbose=False)
# ci = lmfit.conf_interval(mini)
lmfit.printfuncs.report_ci(ci)


# In[12]:

print ci.values()


# In[13]:

a,b,prob = trace['a']['a'], trace['a']['b'], trace['a']['prob']

cx, cy, grid = lmfit.conf_interval2d(mini,  'a','b',30,30)
plt.contourf(cx, cy, grid, np.linspace(0,1,11))
plt.xlabel('a')
plt.colorbar()
plt.ylabel('b')


# # Other ways to do Gaussian fitting
# ## use the astropy.modeling
# astropy provides full documentation on their website
# ```python
# from astropy.modeling import models
# blablabla
# ```
# 
# ## use the scipy.optimize
# ```python
# import scipy.optimize as opt
# opt.minimize(...)
# ```
# 
# # Conclusion:
# ## I am too lazy, so I use *lmfit* which provides simple error estimations
# 

# In[ ]:



