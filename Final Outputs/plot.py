#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Load data from txt file (d = depth, p = profile)
f_dd = 'depth_dose_5x5.txt'
f_d_uncert = 'depth 5x5 uncert.txt'
f_pd1 = 'dose_profile_5x5.txt'
#f_pd2 = 'gp2_30-Dose.txt'
#f_pd3 = 'gp3_30-Dose.txt'
f_p_uncert = 'profile 1 uncert.txt'

d_dose = np.loadtxt(f_dd)
d_uncert = np.loadtxt(f_d_uncert)
p_dose1 = np.loadtxt(f_pd1)
#p_dose2 = np.loadtxt(f_pd2)
#p_dose3 = np.loadtxt(f_pd3)
p_uncert = np.loadtxt(f_p_uncert)

#reverse the array since the list is recorded in reverse order, considering the phantom is in negative z direction
d_dose = d_dose[::-1]
d_uncert = d_uncert[::-1]
# -----------------------------------------------------------------------------
# Declare a figure with 2 rows
fig, ax = plt.subplots(ncols=1, nrows=2, figsize=(10, 12))

# X values from 0 to 100 every 1
n = len(d_dose)
x = np.linspace(0, 50, n)

# First curve, gamma depth in green
y = d_dose

a = ax[0]
c1 = a.plot(x, y, 'g-', label='dose along transverse plane', linewidth=2)

# Second curve, gamma uncertainty in blue, share the same x axis, but use a
# different y axis
y = d_uncert
ax2 = a.twinx()
c2 = ax2.plot(x, y, 'r-', label='$\sigma$ (uncertainty)')
ax2.set_ylim([0.01,0.1])


# Add the legend and the title
lns = c1 +c2
labs = [l.get_label() for l in lns]
a.legend(lns, labs, loc=0)
a.set_title('Percentage Depth Dose')
a.set_xlabel('Depth in water in cm')
a.set_ylabel('PDD (%)')
ax2.set_ylabel('Uncertainty')

# Third curve, gamma profile in green
y = p_dose1*100
a = ax[1]
c3 = a.plot(x, y, 'g-', label='dose at depth 50 mm', linewidth=2)

#y = p_dose2*100
#ax2 = a.twinx()
#c4 = ax2.plot(x,y,'m-',label='dose at depth 100 mm')

#y = p_dose3*100
#ax3 = a.twinx()
#c5 = ax3.plot(x,y,'b-',label='dose at depth 200 mm')

# Last curve, gamma uncertainty profile
y = p_uncert
ax5 = a.twinx()
c6 = ax5.plot(x, y, 'r-', label='$\sigma$ (uncertainty)')

#more curves, gamma profile


# Add the legend and the title
lns = c3 + c6 #+c4+c5 #+c6
labs = [l.get_label() for l in lns]
a.legend(lns, labs, loc=0)
a.set_title('Dose profile')
a.set_xlabel('Off axis distance in cm')
a.set_ylabel('Relative Dose (%)')
ax5.set_ylabel('Uncertainty')

# Show the figure
plt.show()