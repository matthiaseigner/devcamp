import pandas as pd
import numpy as np

def load_data():
  return pd.read_csv('ects.csv')

if __name__ == "__main__": 
  ects_df = load_data()

  ects_without_headers_df = ects_df.dropna(subset=['ECTS'])

  print(ects_without_headers_df[['Prüfung']])