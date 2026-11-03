import data_loader
import pandas as pd

file_path = input("Enter the file path: ")
df = data_loader.load_file(file_path)
df = data_loader.clean_data(df)

print(df.head())