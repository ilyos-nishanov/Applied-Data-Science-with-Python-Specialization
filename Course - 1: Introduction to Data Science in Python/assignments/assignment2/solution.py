import pandas as pd
import numpy as np
import re
#Write a function called proportion_of_education which returns the proportion of children in the
#dataset who had a mother with the education levels equal to less than high school (<12), high school (12),
##more than high school but not a college graduate (>12) and college degree.

#This function should return a dictionary in the form of (use the correct numbers, do not round numbers):

    # {"less than high school":0.2,
    # "high school":0.4,
    # "more than high school but not college":0.2,
    # "college":0.2}

def proportion_of_education ():
    df = pd.read_csv('assets/NISPUF17.csv')
    df = df[['EDUC1']]
    df = df.dropna()
    df = df.sort_values(by=['EDUC1'])
    df = df.reset_index(drop=True)
    df = df['EDUC1'].value_counts()
    df = df.sort_index()
    df = df/len(df)
    df = df.to_dict()
    return df
print(proportion_of_education())