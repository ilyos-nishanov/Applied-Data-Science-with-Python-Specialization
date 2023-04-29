import pandas as pd
import numpy as np
import scipy.stats as stats
import re



#correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella)

def average_influenza_doses():
    df = pd.read_csv('assets/NISPUF17.csv')
    df_bf = df[df['CBF_01'] == 1]
    df_nbf = df[df['CBF_01'] == 2]
    bf = df_bf['P_NUMFLU'].mean()
    round(bf, 1)
    nbf = df_nbf['P_NUMFLU'].mean()
    round(nbf, 1)
    return (bf, nbf)
    raise NotImplementedError()
average_influenza_doses()