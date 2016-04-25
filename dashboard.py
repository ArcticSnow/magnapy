#!/usr/bin/env python

__author__ = "Simon Filhol"
__date__ = "24 April 2016"
__copyright__ = "Copyright 2016"
__license__ = "GNU GPL v3"
__version__ = "1.0"
__email__ = "svfilhol@alaska.edu"

'''
Script to plot basic dashboards of magnaprobe data

'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec


def load_data(filename):
    data = pd.read_csv(filename)

def basic_dash(data):
    # plot data
    fig = plt.figure(figsize=(8, 6))
    gs = gridspec.GridSpec(5, 1)
    ax0 = plt.subplot(gs[0:4])
    pl = ax0.scatter(data['east_utm_m'], data['north_utm_m'] , c=data['snowdepth_cm'], s=50, edgecolor='none')
    fig.colorbar(pl,  orientation='vertical')
    ax1 = plt.subplot(gs[4])
    ax1.hist(data['snowdepth_cm'], bins=25)
    ax0.set_title('Snow depth Map (cm)')
    ax1.set_title('Snow Depth Histogram (cm)')

    plt.tight_layout()



