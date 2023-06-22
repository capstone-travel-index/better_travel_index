#Function to transform esg Table
import pandas as pd

def melt_pivot(df, var=['iso3', 'ind'], value=['2012', '2013','2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']):
    df_mel = pd.melt(df, 
                    id_vars=var, 
                    value_vars=value
                    )
    df_pivoted = df_mel.pivot_table(index=['iso3', 'variable'], columns='ind', values='value', dropna=False).reset_index()
    return df_pivoted