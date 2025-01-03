import pandas as pd
import numpy as np
from Clean_CD import *

# The goal in this script is to create a DataFrame with other major currencies
# Then join it to our cleaned DataFrame and perform the price conversion to get 
# prices for each car in all major currencies.
# US to Euro Conversion rate as of 10/31/24: 0.92
# US to GBP Conversion rate as of 10/31/24: 0.78
# US to Yen Conversion rate as of 10/31/24: 152.00

def converted_DataFrame():
    # Create data with 10,000 sequential IDs, currencies and their exchange rates.
    conversion_df = pd.DataFrame({
        'ID': np.arange(1, 10001),
        'EUR': 0.92,
        'GBP': 0.78,
        'JPY': 152.00
    })

    # Join/ Merge clean_CD with conversion_df on unique sequential IDs
    multi_curr_df = pd.merge(clean_CD(), conversion_df, on='ID', how='left')

    # Perform the currency conversion calculations.
    multi_curr_df['EUR'] = multi_curr_df['USD'] * multi_curr_df['EUR']
    multi_curr_df['GBP'] = multi_curr_df['USD'] * multi_curr_df['GBP']
    multi_curr_df['JPY'] = multi_curr_df['USD'] * multi_curr_df['JPY']

    '''
    pd.set_option('display.max_columns', None) 
    print(conversion_df.head())
    print(multi_curr_df.head())
    '''

    return multi_curr_df