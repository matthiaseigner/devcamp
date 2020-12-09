import pandas as pd
import numpy as np
import datetime
from dateutil.parser import parse

def load_data():
  return pd.read_csv('ects.csv')

if __name__ == "__main__": 
  ects_df = load_data()

  ects_without_headers_df = ects_df.dropna(subset=['ECTS'])

  def get_semester(x):
    timestamp = pd.Timestamp(parse(x).strftime('%Y-%m-%d'))

    semester = 'SS'
    if timestamp.month > 8:
      semester = 'WS'

    return f"{timestamp.year} {semester}"

  ects_without_headers_df['Semester'] = ects_without_headers_df['Datum'].apply(get_semester)

  print(ects_without_headers_df)


  # Mache eine Spalte 'size', die Lehrveranstaltungen mit mehr als 3 als groß, mit weniger als 3 ECTS als klein bezeichnet!
  # meint '<' eh kleiner-gleich? sonst würde ja etwas ausgeschlossen werden oder? 
  
  def get_size(x):
    size = pd.size

    size = 'groß'
    if 'ECTS' > 3:
      size = 'klein'

    return f"{size}"

  ects_without_headers_2_df['size'] = ects_without_headers_df['ECTS'].apply(get_size)
  print(ects_without_headers_2_df)