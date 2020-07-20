#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab as py
import pandas as pd
import CovidFunctions as cf

df_CA = cf.State_TS('California')
df_AZ = cf.State_TS('Arizona')
df_TX = cf.State_TS('Texas')
df_NY = cf.State_TS('New York')
df_FL = cf.State_TS('Florida')

py.figure('Confirmed Cases Comparison', figsize=[16.0, 6.0])
py.title('AZ and CA Confirmed Cases Comparison')
py.plot_date(x=df_CA['Date'],y=df_CA['Total Cases'], 
             label='California', marker='.')
py.plot_date(x=df_AZ['Date'],y=df_AZ['Total Cases'],
             label='Arizona', marker='.')
py.plot_date(x=df_TX['Date'],y=df_TX['Total Cases'],
             label='Texas', marker='.')
py.plot_date(x=df_NY['Date'],y=df_NY['Total Cases'],
             label='New York', marker='.')
py.plot_date(x=df_FL['Date'],y=df_FL['Total Cases'],
             label='Florida', marker='.')
py.xlabel('Dates'), py.ylabel('Confirmed Cases'), py.legend(fontsize='large')
py.xticks(rotation=90), py.grid(), py.tight_layout()
py.autoscale(enable=True, axis='x', tight=True)
py.show()

py.figure('New Cases Per Day', figsize=[16.0, 6.0])
py.title('New Cases Comparison')
py.plot_date(x=df_CA['Date'],y=df_CA['New Cases'], 
             label='California', marker='.')
py.plot_date(x=df_AZ['Date'],y=df_AZ['New Cases'],
             label='Arizona', marker='.')
py.plot_date(x=df_TX['Date'],y=df_TX['New Cases'],
             label='Texas', marker='.')
py.plot_date(x=df_NY['Date'],y=df_NY['New Cases'],
             label='New York', marker='.')
py.plot_date(x=df_FL['Date'],y=df_FL['New Cases'],
             label='Florida', marker='.')
py.xlabel('Dates'), py.ylabel('New Cases'), py.legend(fontsize='large')
py.xticks(rotation=90), py.grid(), py.tight_layout()
py.autoscale(enable=True, axis='x', tight=True)
py.show()

py.figure('New Deaths', figsize=[16.0, 6.0])
py.title('New Deaths Comparison')
py.plot_date(x=df_CA['Date'],y=df_CA['New Deaths'], 
             label='California', marker='.')
py.plot_date(x=df_AZ['Date'],y=df_AZ['New Deaths'],
             label='Arizona', marker='.')
py.plot_date(x=df_TX['Date'],y=df_TX['New Deaths'],
             label='Texas', marker='.')
py.plot_date(x=df_NY['Date'],y=df_NY['New Deaths'],
             label='New York', marker='.')
py.plot_date(x=df_FL['Date'],y=df_FL['New Deaths'],
             label='Florida', marker='.')
py.xlabel('Dates'), py.ylabel('New Deaths'), py.legend(fontsize='large')
py.xticks(rotation=90), py.grid(), py.tight_layout()
py.autoscale(enable=True, axis='x')
py.show()

py.figure('Total Deaths', figsize=[16.0, 6.0])
py.title('Total Deaths Comparison')
py.plot_date(x=df_CA['Date'],y=df_CA['Total Deaths'], 
             label='California', marker='.')
py.plot_date(x=df_AZ['Date'],y=df_AZ['Total Deaths'],
             label='Arizona', marker='.')
py.plot_date(x=df_TX['Date'],y=df_TX['Total Deaths'],
             label='Texas', marker='.')
py.plot_date(x=df_NY['Date'],y=df_NY['Total Deaths'],
             label='New York', marker='.')
py.plot_date(x=df_FL['Date'],y=df_FL['Total Deaths'],
             label='Florida', marker='.')
py.xlabel('Dates'), py.ylabel('Total Deaths'), py.legend(fontsize='large')
py.xticks(rotation=90), py.grid(), py.tight_layout()
py.autoscale(enable=True, axis='x')
py.show()

