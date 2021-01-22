import pandas as pd
import numpy as np
import datetime
from dateutil.parser import parse

def load_data():
  return pd.read_csv('ects.csv')

if __name__ == "__main__": 
  ects_df = load_data()

  # remove headers
  ects_without_headers_df = ects_df.dropna(subset=['ECTS'])

  # print the count of exams per teacher
  ects_without_headers_df = ects_without_headers_df[~(ects_without_headers_df['Note'] == '+')]
  ects_without_headers_df['Note'] = ects_without_headers_df['Note'].astype(int)

  semesters_df = ects_without_headers_df.groupby(['Prüfer/Prüferin']).agg({'Prüfer/Prüferin':'count', 'ECTS': 'sum', 'SSt.': 'sum', 'Note': 'mean'})
  semesters_df = semesters_df.rename(columns={'Prüfer/Prüferin': 'count'})
  print(semesters_df[semesters_df['count']>1].sort_values(by=['count'], ascending=False))

  # https://population.un.org/wpp/Download/Standard/CSV/
  # https://towardsdatascience.com/analysing-and-visualising-the-country-wise-population-from-1955-to-2020-with-pandas-matplotlib-70b3614eed6b