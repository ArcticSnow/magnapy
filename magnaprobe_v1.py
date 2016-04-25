#!/usr/bin/env python

__author__ = "Simon Filhol"
__date__ = "22 April 2016"
__copyright__ = "Copyright 2007"
__license__ = "GNU GPL v3"
__version__ = "1.0"
__email__ = "svfilhol@alaska.edu"

import pyproj as pj
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec


# Feature to add
#   - include the datetime column in final file
#   - find out how to add metadata to final file
#   - structure next version to for running script from terminal based on arguments


# open clean magnaprobe data
data = pd.read_csv('/Users/tintino/PhD/Snow_Projects/Imnavait2016/20160422_imnavait_diagonal.csv')

# convert from lat/long to UTM 6N
proj_latlon = pj.Proj("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")
proj_utm = pj.Proj("+proj=utm +zone=6 +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
data['lat'] = data['latitude_a'].values + data['latitude_b'].values/100
data['lon'] = data['Longitude_a'].values + data['Longitude_b'].values/100
x_utm, y_utm = pj.transform(proj_latlon, proj_utm, data['lon'].values,  data['lat'].values)

# save dataframe to csv
dfinal = pd.DataFrame()
dfinal['timestamp'] = data['TIMESTAMP']
dfinal['north_utm_m'] = y_utm
dfinal['east_utm_m'] = x_utm
dfinal['snowdepth_cm'] = data['DepthCm']

dfinal.to_csv('magna_probe_data_here.csv')

# plot data
fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(5, 1)
ax0 = plt.subplot(gs[0:4])
pl = ax0.scatter(x_utm, y_utm , c=data['DepthCm'], s=50, edgecolor='none')
fig.colorbar(pl,  orientation='vertical')
ax1 = plt.subplot(gs[4])
ax1.hist(data['DepthCm'], bins=25)
ax0.set_title('Snow depth Map (cm)')
ax1.set_title('Snow Depth Histogram (cm)')

plt.tight_layout()





