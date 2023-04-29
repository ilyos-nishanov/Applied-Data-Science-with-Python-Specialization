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

# Return a tuple of the average number of influenza vaccines for those children we know
# received breastmilk as a child and those who know did not.
# This function should return a tuple in the form (use the correct numbers:(2.5, 0.1)

def average_influenza_doses():
    df = pd.read_csv('assets/NISPUF17.csv')
    df_bf = df[df['CBF_01'] == 1]
    df_nbf = df[df['CBF_01'] == 2]
    bf = df_bf['P_NUMFLU'].mean()
    # round it to 1 decimal places
    bf = round(bf,1)
    nbf = df_nbf['P_NUMFLU'].mean()
    # round it to 1 decimal places
    nbf = round(nbf,1)
    return (bf, nbf)
print(average_influenza_doses())

# Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.
# This function should return a dictionary in the form of (use the correct numbers):
# {'male':0.2, 'female':0.4}

def chickenpox_by_sex():
    df=pd.read_csv('assets/NISPUF17.csv')
    cpo_sex=df[df['P_NUMVRC'].gt(0) & df['HAD_CPOX'].lt(3)].loc[:,['HAD_CPOX','SEX']]
    cpo1_sex1=len(cpo_sex[(cpo_sex['HAD_CPOX']==1) & (cpo_sex['SEX']==1)])
    cpo1_sex2=len(cpo_sex[(cpo_sex['HAD_CPOX']==1) & (cpo_sex['SEX']==2)])
    cpo2_sex1=len(cpo_sex[(cpo_sex['HAD_CPOX']==2) & (cpo_sex['SEX']==1)])
    cpo2_sex2=len(cpo_sex[(cpo_sex['HAD_CPOX']==2) & (cpo_sex['SEX']==2)])

    cbs={"male":0,
        "female":0}
    cbs['male']=round(cpo1_sex1/cpo2_sex1,1)
    cbs['female']=round(cpo1_sex2/cpo2_sex2,1)
    return cbs
print(chickenpox_by_sex())