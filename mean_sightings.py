#!/usr/bin/env python

import numpy as np
import matplotlib.mlab as ml
import sys

def get_sightings(filename, focusbiosig):
    # load file
    table = ml.csv2rec(filename)
    
    #make biosig case-insensitive - capital letter initially only
    focusbiosig = focusbiosig.capitalize()

    # find number of reports in boolean array
    #isfocus = (table['biosignature'] == focusbiosig)
    #totalrecs = np.sum(isfocus)
    # or do it this way...
    totalrecs = totalcount = 0.0
    for rec in table:
        if rec['biosignature'] == focusbiosig:
            totalrecs += 1
            totalcount += rec['count']

    if totalrecs > 0:
        #mean_sigs = np.mean(table['count'][isfocus])
        mean_sigs = totalcount/totalrecs
    else:
        mean_sigs = 0

    return totalrecs, mean_sigs

# END function get_sightings()
#=========================================================

#these lines first to run in python command
#filename = 'sightings_tab_sm.csv'
#focusbiosig = 'Water'
#print get_sightings(filename, focusbiosig)

#then this
if __name__ == '__main__':
    #filename = 'sightings_tab_sm.csv'
    filename = sys.argv[1]
    #focusbiosig = 'Water'
    focusbiosig = sys.argv[2]
    print get_sightings(filename, focusbiosig)

