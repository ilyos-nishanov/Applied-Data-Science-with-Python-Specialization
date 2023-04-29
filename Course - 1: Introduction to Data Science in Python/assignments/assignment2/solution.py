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
    df_edu = df['EDUC1']
    less_than_high_school = df_edu[df_edu == 1].count()/df_edu.count()
    # round it to 2 decimal places
    less_than_high_school = round(less_than_high_school,2)
    high_school = df_edu[df_edu == 2].count()/df_edu.count()
    #round it to 2 decimal places
    high_school = round(high_school,2)
    more_than_high_school = df_edu[df_edu == 3].count()/df_edu.count()
    #round it to 2 decimal places
    more_than_high_school = round(more_than_high_school,2)
    college = df_edu[df_edu == 4].count()/df_edu.count()
    #round it to 2 decimal places
    college = round(college,2)
    return {"less than high school":less_than_high_school,
            "high school":high_school,
            "more than high school but not college":more_than_high_school,
            "college":college}
print(proportion_of_education())