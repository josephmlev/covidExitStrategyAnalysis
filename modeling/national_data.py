#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pylab as py
import pandas as pd
import CovidFunctions as cf

df_CA = cf.State_df('California')
df_AZ = cf.State_df('Arizona')
df_TX = cf.State_df('Texas')
df_NY = cf.State_df('New York')
df_FL = cf.State_df('Florida')

# Plot The C cases in CA and AZ
py.figure('Confirmed Cases Comparison', figsize=[16.0, 6.0])
py.title('AZ and CA Confirmed Cases Comparison')
py.plot_date(x=df_CA['Date'],y=df_CA['Total Cases'], 
             label='California', marker='.', linestyle='-')
py.plot_date(x=df_AZ['Date'],y=df_AZ['Total Cases'],
             label='Arizona', marker='.', linestyle='-')
py.plot_date(x=df_TX['Date'],y=df_TX['Total Cases'],
             label='Texas', marker='.', linestyle='-')
py.plot_date(x=df_NY['Date'],y=df_NY['Total Cases'],
             label='New York', marker='.', linestyle='-')
py.plot_date(x=df_FL['Date'],y=df_FL['Total Cases'],
             label='Florida', marker='.', linestyle='-')
py.xlabel('Dates'), py.ylabel('Confirmed Cases'), py.legend(fontsize='large')
py.xticks(rotation=90), py.grid(), py.tight_layout()
py.autoscale(enable=True, axis='x', tight=True)
py.show()


# Plot New Cases per day
# Plot The C cases in CA and AZ
py.figure('New Cases Per Day', figsize=[16.0, 6.0])
py.title('New Cases Comparison')
py.plot_date(x=df_CA['Date'],y=df_CA['New Cases'], 
             label='California', marker='.', linestyle='-')
py.plot_date(x=df_AZ['Date'],y=df_AZ['New Cases'],
             label='Arizona', marker='.', linestyle='-')
py.plot_date(x=df_TX['Date'],y=df_TX['New Cases'],
             label='Texas', marker='.', linestyle='-')
py.plot_date(x=df_NY['Date'],y=df_NY['New Cases'],
             label='New York', marker='.', linestyle='-')
py.plot_date(x=df_FL['Date'],y=df_FL['New Cases'],
             label='Florida', marker='.', linestyle='-')
py.xlabel('Dates'), py.ylabel('New Cases'), py.legend(fontsize='large')
py.xticks(rotation=90), py.grid(), py.tight_layout()
py.autoscale(enable=True, axis='x', tight=True)
py.show()

# Plot New Deaths
# Plot The C cases in CA and AZ
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
py.autoscale(enable=True, axis='x', tight=True)
py.show()
