import pandas as pd
import numpy as np

# Filter all warnings. If you would like to see the warnings, please comment the two lines below.
import warnings
warnings.filterwarnings('ignore')

def answer_one():
    Energy = pd.read_excel('assets/Energy Indicators.xls',na_values=["..."],header = None,skiprows=18,skipfooter= 38,usecols=[2,3,4,5],names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
    Energy['Energy Supply'] = Energy['Energy Supply'].apply(lambda x: x*1000000)
    Energy['Country'] = Energy['Country'].str.replace(r" \(.*\)","")
    Energy['Country'] = Energy['Country'].str.replace(r"\d+","")
    Energy['Country'] = Energy['Country'].replace({"Republic of Korea": "South Korea","United States of America": "United States","United Kingdom of Great Britain and Northern Ireland": "United Kingdom","China, Hong Kong Special Administrative Region": "Hong Kong"})
    GDP = pd.read_csv('assets/world_bank.csv',skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace({"Korea, Rep.": "South Korea","Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"})
    ScimEn = pd.read_excel('assets/scimagojr-3.xlsx')
    df = pd.merge(ScimEn,Energy,how='inner',left_on='Country',right_on='Country')
    df = df[df['Rank']<=15]

    df = pd.merge(df,GDP,how='inner',left_on='Country',right_on='Country Name')
    df = df.set_index('Country')
    df = df[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index','Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007','2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    # df = df.sort_values(by='Rank')
    return df
answer_one()

def answer_two():
    Energy = pd.read_excel('assets/Energy Indicators.xls',na_values=["..."],header = None,skiprows=18,skipfooter= 38,usecols=[2,3,4,5],names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])
    Energy['Energy Supply'] = Energy['Energy Supply'].apply(lambda x: x*1000000)
    Energy['Country'] = Energy['Country'].str.replace(r" \(.*\)","")
    Energy['Country'] = Energy['Country'].str.replace(r"\d+","")
    Energy['Country'] = Energy['Country'].replace({"Republic of Korea": "South Korea","United States of America": "United States","United Kingdom of Great Britain and Northern Ireland": "United Kingdom","China, Hong Kong Special Administrative Region": "Hong Kong"})
    GDP = pd.read_csv('assets/world_bank.csv',skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace({"Korea, Rep.": "South Korea","Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"})
    GDP = GDP.rename(columns={'Country Name': 'Country'})
    GDP = GDP.loc[:,['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    ScimEn = pd.read_excel('assets/scimagojr-3.xlsx')
    df = pd.merge(ScimEn,Energy,how='inner',left_on='Country',right_on='Country')
    inner_join_1 = pd.merge(df,GDP,how='inner',left_on='Country',right_on='Country')
    inner_join_0 = pd.merge(ScimEn,Energy,how='inner',left_on='Country',right_on='Country')
    outer_join_1 = pd.merge(inner_join_1,inner_join_2,how='outer',left_on='Country',right_on='Country')
    outer_join_2 = pd.merge(inner_join_2,inner_join_1,how='outer',left_on='Country',right_on='Country')
    return len(outer_join_1)-len(outer_join_2)
answer_two()

