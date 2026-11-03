import pandas as pd
import numpy as np
from datetime import datetime

# Function to load data from a CSV file into a pandas DataFrame
def load_file(file_path):
    return pd.read_csv(file_path)


def clean_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.dropna()
    return df


