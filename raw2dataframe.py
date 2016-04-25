#!/usr/bin/env python

__author__ = "Simon Filhol"
__date__ = "22 April 2016"
__copyright__ = "Copyright 2016"
__license__ = "GNU GPL v3"
__version__ = "1.0"
__email__ = "svfilhol@alaska.edu"

'''
Script to:

1 - Extract relevant information (time, location, depth) from magnaprobe
file after basic cleaning and saved as .csv with first and 2nd line removed.

2 - Convert lat/long to UTM (6N by default) coordinate system.

3 - Save the data to a new file readable directly with plotting functions.


Feature to add
   - find out how to add metadata to final file or use Pickle to save files
   - structure next version to for running script from terminal based on arguments
'''

import pyproj as pj
import pandas as pd


def raw2csv():

class magna_data(object):
    def __init__(self):
        self.depth =
        self.north =
        self.east =
        self.lat =
        self.long =
        self.snowdepth =
        self.date =
        self.pointID =
        self.timestamp =
        self.



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
