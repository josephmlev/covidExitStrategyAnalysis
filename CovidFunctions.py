#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Functions supporting Covid research.

files downloaded off JHU GitHub: https://github.com/CSSEGISandData/COVID-19

The first set of functions return dataframes from raw time series data. 

Author: Steven Sheppard
Date:	7/20/20

'''
import pylab as py
import pandas as pd
from datetime import date

# Specify which state you want data for and return
# a dataframe.

filename_c = 'Data/time_series_covid19_confirmed_US.csv' 
filename_d = 'Data/time_series_covid19_deaths_US.csv'


# Returns a data frame with time series data for total and new cases and deaths.
def State_df(state):
    # The only columns needed are the dates, numbers and Location ID
    df_c = pd.read_csv(filename_c).drop(columns=[
            'UID', 'iso2', 'iso3', 'code3', 'Lat', 'Long_','Combined_Key',
            'Country_Region', 'Admin2', 'FIPS'])
    
    # Locate the requested state then drop ID column and sum over all regions
    df_c = df_c.loc[df_c['Province_State'] == state].drop(columns=['Province_State']).sum(axis=0)
    df_c = pd.DataFrame(df_c) # needed or df is a series
    
    df_c['New Cases'] = df_c.diff(1).fillna(0) #create a new column for the number of new cases.
    
    df_c.reset_index(level=0, inplace=True) # Moves the dates from a row name to new column
    df_c = df_c.rename(columns={'index':'Date', 0:"Total Cases"}) #rename the columns 
    
    df_c['Date'] = pd.to_datetime(df_c['Date'], format='%m%d%Y', errors='ignore') # change the date format
    
    # Now to do the samething for the deaths df
    df_d = pd.read_csv(filename_d).drop(columns=[
            'UID', 'iso2', 'iso3', 'code3', 'Lat', 'Long_','Combined_Key',
            'Country_Region', 'Admin2', 'FIPS', 'Population'])
    
    df_d = df_d.loc[df_d['Province_State'] == state].drop(columns=['Province_State']).sum(axis=0)
    df_d = pd.DataFrame(df_d) # needed or df is a series
    
    df_d['New Deaths'] = df_d.diff(1).fillna(0) #create a new column for the number of new cases.
    
    df_d.reset_index(level=0, inplace=True) # Moves the dates from a row name to new column
    df_d = df_d.rename(columns={'index':'Date', 0:"Total Deaths"}) #rename the columns
    df_d['Date'] = pd.to_datetime(df_d['Date'], format='%m%d%Y', errors='ignore') # change the date format
    
    #Merge the cases and deaths into one Dataframe
    df = pd.merge(df_c, df_d, how='left')
    
    return df

# Returns a plot of the input data, this is specific to time series data.


