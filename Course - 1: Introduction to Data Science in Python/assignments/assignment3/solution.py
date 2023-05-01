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
    df_inner = pd.merge(ScimEn,Energy,how='inner',left_on='Country',right_on='Country')
    df_inner = pd.merge(df_inner,GDP,how='inner',left_on='Country',right_on='Country')
    df_outer = pd.merge(ScimEn,Energy,how='outer',left_on='Country',right_on='Country')
    df_outer = pd.merge(df_outer,GDP,how='outer',left_on='Country',right_on='Country')
    return len(df_outer)-len(df_inner)
answer_two()


def answer_three():
    Top15 = answer_one()
    avgGDP = Top15.loc[:,'2006':'2015'].mean(axis=1)
    avgGDP = avgGDP.sort_values(ascending=False)
    return avgGDP
answer_three()

def answer_four():
    Top15 = answer_one()
    avgGDP = answer_three()
    return Top15.loc[avgGDP.index[5],'2015']-Top15.loc[avgGDP.index[5],'2006']
answer_four()

def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()
answer_five()

def answer_six():
    #What country has the maximum % Renewable and what is the percentage?
    answer = answer_one().sort_values(by='% Renewable',ascending=False).iloc[0]
    (country, percentage) = (answer.name, answer['% Renewable'])
    return (country, percentage)
answer_six()

def answer_seven():
    Top15 = answer_one()
    Top15['Ratio'] = Top15['Self-citations']/Top15['Citations']
    answer = Top15.sort_values(by='Ratio',ascending=False).iloc[0]
    (country, ratio) = (answer.name, answer['Ratio'])
    return (country, ratio)
answer_seven()

def answer_eight():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    answer = Top15.sort_values(by='Population',ascending=False).iloc[2]
    (country, population) = (answer.name, answer['Population'])
    return country
answer_eight()

def answer_nine():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['Citable documents per Capita'] = Top15['Citable documents']/Top15['Population']
    return Top15['Citable documents per Capita'].corr(Top15['Energy Supply per Capita'])
answer_nine()

def answer_ten():
    #Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
    Top15 = answer_one()
    Top15['Median'] = Top15['% Renewable'].median()

    def above_median(row):
        if row['% Renewable'] >= row['Median']:
            row['HighRenew'] = 1
        else:
            row['HighRenew'] = 0
        return row

    Top15 = Top15.apply(above_median,axis=1)
    return Top15['HighRenew']
answer_ten()

def answer_eleven():
    ContinentDict  = {'China':'Asia',
                        'United States':'North America',
                        'Japan':'Asia',
                        'United Kingdom':'Europe',
                        'Russian Federation':'Europe',
                        'Canada':'North America',
                        'Germany':'Europe',
                        'India':'Asia',
                        'France':'Europe',
                        'South Korea':'Asia',
                        'Italy':'Europe',
                        'Spain':'Europe',
                        'Iran':'Asia',
                        'Australia':'Australia',
                        'Brazil':'South America'}
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['Continent'] = Top15.index.to_series().map(ContinentDict)
    Top15 = Top15.reset_index()
    Top15 = Top15.set_index('Continent')
    Top15 = Top15.groupby(level=0)['Population'].agg({'size': np.size, 'sum': np.sum, 'mean': np.mean,'std': np.std})
    return Top15
answer_eleven()
