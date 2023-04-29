import pandas as pd
import numpy as np

df = pd.read_csv('assets/NISPUF17.csv')

#Write a function called proportion_of_education which returns the proportion of children in the
#dataset who had a mother with the education levels equal to less than high school (<12), high school (12),
##more than high school but not a college graduate (>12) and college degree.

#This function should return a dictionary in the form of (use the correct numbers, do not round numbers):

    # {"less than high school":0.2,
    # "high school":0.4,
    # "more than high school but not college":0.2,
    # "college":0.2}

def proportion_of_education ()