import pandas as pd

def clean_CD():
    df = pd.read_csv('Car_Data.csv')

    # I already know after viewing the data there are no null values but we will still perform this operation for best practice purposes.
    # Keep original DataFrame but drop all null values.
    df.dropna(inplace = True)

    # Ensure that ID field is a unique identifier.
    df.drop_duplicates(subset='ID', inplace = True)

    # Change the column name 'Price' to USD to combine with conversion table.
    df.rename(columns = {'Price':'USD'}, inplace = True)

    # Convert USD column to Float data type for accurate conversions.
    df['USD'] = df['USD'].astype(float)

    # Create view to check cleaned data.
    
    '''clean_view = df.head(25)
    pd.set_option('display.max_columns', None) 
    print(clean_view)'''

    # Export cleaned DataFrame
    return df