#Function to transform esg Table
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def melt_pivot(df, var=['iso3', 'ind'], value=['2012', '2013','2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']):
    df_mel = pd.melt(df, 
                    id_vars=var, 
                    value_vars=value
                    )
    df_pivoted = df_mel.pivot_table(index=['iso3', 'variable'], columns='ind', values='value', dropna=False).reset_index()
    return df_pivoted

def interpol(df, ind_lst):
    indicators = ind_lst
    # Iterate over unique iso3 values/countries
    for iso3 in df['iso3'].unique():
        # Create a boolean mask to select rows for the current country
        mask = df['iso3'] == iso3
        
        # Iterate over the columns/indicators
        for indicator in indicators:
            # Perform linear interpolation for the current country only
            df.loc[mask, indicator] = df.loc[mask, indicator].interpolate(method='linear', limit_direction='both')
    return df

def lin_reg(df, ind_lst):
    # Define the columns for linear regression
    indicators = ind_lst
    # Iterate over unique iso3 values/countries
    for iso3 in df['iso3'].unique():
        # Iterate over columns/indicators
        for indicator in indicators:
            # Filter rows for the current iso3 and indicator
            filtered_rows = df[(df['iso3'] == iso3) & (df[indicator].notna())]
            
            # Check if there are enough non-NaN values for regression
            if len(filtered_rows) >= 2:
                X = filtered_rows['variable'].values.reshape(-1, 1)
                y = filtered_rows[indicator].values.reshape(-1, 1)
                
                # Create a regression model and fit it
                regression_model = LinearRegression()
                regression_model.fit(X, y)
                
                # Predict NaN values using the regression model
                X_pred = df.loc[(df['iso3'] == iso3) & (df[indicator].isna()), 'variable'].values.reshape(-1, 1)
                
                if len(X_pred) > 0:
                    y_pred = regression_model.predict(X_pred)
                    
                    # Replace NaN values with the predicted values
                    df.loc[(df['iso3'] == iso3) & (df[indicator].isna()), indicator] = np.squeeze(y_pred)
    return df

##Auflistung aller country-indicator-Kmobinationen wo alle Jahre leer sind
def nan_scanner_comb(df):
    # Liste zum Speichern der Spaltennamen und iso3-Werte
    empty_columns = []

    # Iteriere über eindeutige iso3-Werte/Länder
    for iso3 in df['iso3'].unique():
        # Überprüfe für jede Spalte, ob alle Werte in der Spalte "variable" leer sind
        for column in df.columns:
            if df.loc[df['iso3'] == iso3, column].isnull().any():
                # Füge Spaltenname und iso3-Wert zur Liste hinzu
                empty_columns.append((iso3, column))

    # Erstelle ein DataFrame mit den Spaltennamen und iso3-Werten
    tabelle_empty_columns = pd.DataFrame(empty_columns, columns=['iso3', 'Spalte'])
    return tabelle_empty_columns

def per_null(df):
    print((df.isnull().sum()/len(df)*100))