
import pandas as pd
import numpy as np
from typing import Dict

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function cleans and formats the column names of the DataFrame.
    
    Inputs:
    df: DataFrame with column names to be cleaned and formatted
    
    Outputs:
    DataFrame with cleaned and formatted column names
    '''
    
    df2 = df.copy()
    
    cleaned_names = []
    for name in df2.columns:
        # Perform cleaning and formatting operations on each column name
        # Modify the conditions and transformations based on your specific requirements
        cleaned_name = name.strip().lower().replace(" ", "_")
        cleaned_names.append(cleaned_name)

    df2.columns = cleaned_names
    
    return df2


def clean_state(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function cleans and formats the 'state' column of the DataFrame.
    It replaces specific state abbreviations with their full names.
    
    Inputs:
    df: DataFrame with a 'state' column to be cleaned and formatted
    
    Outputs:
    DataFrame with the 'state' column cleaned and formatted
    '''
    
    df2 = df.copy()
    
    state_mapping = {
        "WA": "Washington",
        "AZ": "Arizona",
        "Cali": "California"
    }

    df2["st"] = df2["st"].map(state_mapping).fillna(df2["st"])
    return df2


def clean_gender_column(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function cleans the 'gender' column by homogenizeing 
    all values to either 'M' or 'F' according to its first character.
    Unknnown values will be filled with its modal value.
    
    Inputs:
    data: input dataframe that includes a 'gender' column
    
    Outputs:
    DataFrame with a cleaned 'gender' column.
    '''
    df1 = df.copy()
    
    # transform to upper case & homogenize values to M or F according to first character. Unknowns -> mode
    df1['gender'] = [x[0].upper() if type(x) == str and x[0].upper() in ['M', 'F'] else df1['gender'].mode()[0] for x in df1['gender']]

    return df1


def clean_education_column(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function cleans the 'education' column by standardizing values to 'Bachelor' for 'Bachelors' entries.
    
    Inputs:
    df: input dataframe that includes an 'education' column
    
    Outputs:
    DataFrame with a cleaned 'education' column.
    '''
    df1 = df.copy()

    def clean_education(x):
        if x == "Bachelors":
            return "Bachelor"
        else:
            return x
    
    df1['education'] = df1['education'].apply(clean_education)

    return df1


def clean_customer_lifetime_value(df: pd.DataFrame) -> pd.DataFrame:
    df1 = df.copy()
    df1["customer_lifetime_value"]=df1["customer_lifetime_value"].apply(lambda x:float(x.replace("%",""))if pd.notna(x) else x)
    return df1

def clean_numberofopencomplaintsdtype(df: pd.DataFrame) -> pd.DataFrame:
    df1 = df.copy()
    df1["number_of_open_complaints"]=df1["number_of_open_complaints"].apply(lambda x:x[2] if isinstance(x, str) else x)
    
    return df1

def cleaning_datatypes(df: pd.DataFrame) -> pd.DataFrame:
        df1 = df.copy()
        df1.number_of_open_complaints = pd.to_numeric(df1.number_of_open_complaints, errors="coerce",)
        
        return df1

def remove_duplicate_and_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function removes duplicate rows and rows with all the columns empty.
    
    Input:
    df: input DataFrame
    
    Output:
    df: output DataFrame
    '''
    df1 = df.copy()
    
    df1.drop_duplicates(inplace = True) # drop all duplicate rows
    df1.dropna(inplace = True) # drop all empty rows
    
    return df1

def clean_and_format_data(df: pd.DataFrame) -> pd.DataFrame:
    '''
    '''
    df1 = df.copy()
    
    df1 = clean_column_names(df1)
    df1 = clean_state(df1)
    df1 = clean_gender_column(df1)
    df1 = clean_education_column(df1)
    df1 = clean_customer_lifetime_value(df1)
    df1 = clean_numberofopencomplaintsdtype(df1)
    df1 = cleaning_datatypes(df1)
    df1 = remove_duplicate_and_empty_rows(df1)

    return df1










    
