#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Functions supporting Covid research.

files downloaded off JHU GitHub: https://github.com/CSSEGISandData/COVID-19


Author: Steven Sheppard
Date:	7/20/20

'''
import pandas as pd
from datetime import date, timedelta

# Yesterday's data is available today
now = date.today() - timedelta(days=1)
FORMAT = "%m-%d-%Y"
date1 = now.strftime(FORMAT)

# SS: I like the retreval but I would worry about run time if it is used
# in a function that is called very frequently. Maybe there is a work around
# that loads the file when the model is loaded in the preamble.

# filename_c = 'COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
# filename_d = 'COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'

filename_c = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'

filename_d = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'

df_c = pd.read_csv(filename_c).drop(columns=[
    'UID', 'iso2', 'iso3', 'code3', 'Lat', 'Long_', 'Combined_Key',
    'Country_Region', 'Admin2', 'FIPS'])

df_d = pd.read_csv(filename_d).drop(columns=[
    'UID', 'iso2', 'iso3', 'code3', 'Lat', 'Long_', 'Combined_Key',
    'Country_Region', 'Admin2', 'FIPS', 'Population'])

filename_dailyReport = 'COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports_us/' + date1 + '.csv'

# Returns a data frame with time series data for total and new cases and deaths.
# Another function should be made similar to State_TS but more
# particular to the region rather than state.

def state_ts(state, df_raw):
    df_c = df_raw[0]
    df_d = df_raw[1]

    # The only columns needed are the dates, numbers and Location ID
    # Locate the requested state then drop ID column and sum over all regions
    df_c = df_c.loc[df_c['Province_State'] == state].drop(columns=['Province_State']).sum(axis=0)
    df_c = pd.DataFrame(df_c)  # requiered or df is a series
    df_c['New Cases'] = df_c.diff(1).fillna(0)  # new column for # new cases.
    df_c.reset_index(level=0, inplace=True)  # Moves the dates row to col
    df_c = df_c.rename(columns={'index': 'Date', 0: "Total Cases"})

    # Copy and paste, replace 'cases' with 'deaths'
    df_d = df_d.loc[df_d['Province_State'] == state].drop(columns=['Province_State']).sum(axis=0)
    df_d = pd.DataFrame(df_d)
    df_d['New Deaths'] = df_d.diff(1).fillna(0)
    df_d.reset_index(level=0, inplace=True)
    df_d = df_d.rename(columns={'index': 'Date', 0: "Total Deaths"})

    # Merge the cases and deaths into one Dataframe
    df = pd.merge(df_c, df_d, how='left')

    return df


def state_dailyreport(state):
    if isinstance(state) != str:
        return print('State must be a string')
    else:
        return pd.read_csv(filename_dailyReport).loc[state == 'Province_State']
