#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Load data from txt file (d = depth, p = profile)
f_d_edep = 'output/gamma-depth-Edep.txt'
f_d_uncert = 'output/gamma-depth-Edep-Uncertainty.txt'
f_p_edep = 'output/gamma-profile-Edep.txt'
f_p_uncert = 'output/gamma-profile-Edep-Uncertainty.txt'

d_edep = np.loadtxt(f_d_edep)
d_uncert = np.loadtxt(f_d_uncert)
p_edep = np.loadtxt(f_p_edep)
p_uncert = np.loadtxt(f_p_uncert)

# -----------------------------------------------------------------------------
# Declare a figure with 2 rows
fig, ax = plt.subplots(ncols=1, nrows=2, figsize=(10, 12))

# X values from 0 to 100 every 1
x = np.linspace(0, 100, 100)

# First curve, gamma depth in green
y = d_edep
a = ax[0]
c1 = a.plot(x, y, 'g-', label='edep', linewidth=2)

# Second curve, gamma uncertainty in blue, share the same x axis, but use a
# different y axis
y = d_uncert
ax2 = a.twinx()
c2 = ax2.plot(x, y, 'b-', label='$\sigma$ (uncertainty)')

# Add the legend and the title
lns = c1+c2
labs = [l.get_label() for l in lns]
a.legend(lns, labs, loc=0)
a.set_title('Depth deposited energy')
a.set_xlabel('Distance in mm')
a.set_ylabel('Deposited energy in MeV')
ax2.set_ylabel('Uncertainty')

# Third curve, gamma profile in green
y = p_edep
a = ax[1]
c3 = a.plot(x, y, 'g-', label='edep', linewidth=2)

# Last curve, gamma uncertainty profile
y = p_uncert
ax2 = a.twinx()
c4 = ax2.plot(x, y, 'b-', label='$\sigma$ (uncertainty)')

# Add the legend and the title
lns = c3+c4
labs = [l.get_label() for l in lns]
a.legend(lns, labs, loc=0)
a.set_title('Deposited energy profile')
a.set_xlabel('Distance in mm')
a.set_ylabel('Deposited energy in MeV')
ax2.set_ylabel('Uncertainty')

# Show the figure
plt.show()
