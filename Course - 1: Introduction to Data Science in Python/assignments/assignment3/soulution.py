# All questions are weighted the same in this assignment. This assignment requires more individual learning then the last one did - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. All questions are worth the same number of points except question 1 which is worth 20% of the assignment grade.

# **Note**: Questions 2-13 rely on your question 1 answer.

import pandas as pd
import numpy as np


# Load the energy data from the file `assets/Energy Indicators.xls`, which is a list of indicators of [energy supply and renewable electricity production](assets/Energy%20Indicators.xls) from the [United Nations](http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013, and should be put into a DataFrame with the variable name of **Energy**.

# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:

# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]`

# Convert `Energy Supply` to gigajoules (**Note: there are 1,000,000 gigajoules in a petajoule**). For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.

# Rename the following list of countries (for use in later questions):

# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```

# There are also several countries with parenthesis in their name. Be sure to remove these, e.g. `'Bolivia (Plurinational State of)'` should be `'Bolivia'`.

# Next, load the GDP data from the file `assets/world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**.

# Make sure to skip the header, and rename the following list of countries:

# ```"Korea, Rep.": "South Korea",
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```

# Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](http://www.scimagojr.com/countryrank.php?category=2102) from the file `assets/scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.

# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
#        'Citations per document', 'H index', 'Energy Supply',
#        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
#        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

# *This function should return a DataFrame with 20 columns and 15 entries, and the rows of the DataFrame should be sorted by "Rank".*

def load_dataset():
    import re

    # Load the energy data from the file assets/Energy Indicators.xls.
    Energy = pd.read_excel("assets/Energy Indicators.xls", usecols="C:F")

    # exclude the footer and header, and rename the column names
    Energy = Energy[18:245].reset_index(drop=True)
    Energy = Energy.rename(columns={"Unnamed: 2": "Country",
                                    "Unnamed: 3": "Energy Supply",
                                    "Unnamed: 4": "Energy Supply per Capita",
                                    "Unnamed: 5": "% Renewable"})

    # Convert Energy Supply from petajoule to gigajoules
    Energy["Energy Supply"] = Energy["Energy Supply"].replace({"...": np.nan}).apply(lambda x: x*1000000)

    # Rename countries with numbers and/or parenthesis in their name.
    Energy["Country"] = Energy["Country"].apply(lambda x: re.sub("(\s\(.+\))|[0-9]+", "", str(x)))

    # Rename the following list of countries
    Energy["Country"] = Energy["Country"].replace({"Republic of Korea": "South Korea",
                                           "United States of America": "United States",
                                           "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                           "China, Hong Kong Special Administrative Region": "Hong Kong"})


    # Load the GDP data from the file assets/world_bank.csv.
    GDP = pd.read_csv("assets/world_bank.csv", header=4)
    GDP = GDP.rename(columns={"Country Name": "Country"})

    # rename the following list of countries
    GDP["Country"] = GDP["Country"].replace({"Korea, Rep.": "South Korea",
                                              "Iran, Islamic Rep.": "Iran",
                                              "Hong Kong SAR, China": "Hong Kong"})
    GDP = GDP.drop(GDP.columns[1:-10], axis=1)

    # Load the Sciamgo Journal and Country Rank data for Energy from the file assets/scimagojr-3.xlsx
    ScimEn = pd.read_excel("assets/scimagojr-3.xlsx")

    return (Energy, GDP, ScimEn)

def answer_one():

    Energy, GDP, ScimEn = load_dataset()

    # Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names).
    df = pd.merge(ScimEn, Energy, how="inner", left_on="Country", right_on="Country")
    df = pd.merge(df, GDP, how="inner", left_on="Country", right_on="Country")

    # Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank'
    df = df.set_index("Country").sort_values("Rank").iloc[:15]
    df = df.drop(df.columns[10:-1], axis=1)

    return df

