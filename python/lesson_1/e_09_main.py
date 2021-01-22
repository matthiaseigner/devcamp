import pandas as pd
import numpy as np
import datetime
from dateutil.parser import parse
from e_07_main import sum_of_ects

def load_data():
  return pd.read_csv('ects.csv')

if __name__ == "__main__": 
  ects_df = load_data()

  # remove headers
  ects_without_headers_df = ects_df.dropna(subset=['ECTS'])


  # Mache eine Spalte 'size', die Lehrveranstaltungen mit mehr als 3 als groß, mit weniger als oder genau 3 ECTS als klein bezeichnet!
  # konnte das nicht kontrollieren, weil ich nicht herausgefunden habe, wie man gekürzte Dataframes im Terminal ganz anzeigt. 
  def get_size(ects):

    size = 'groß'
    if ects <= 3:
      size = 'klein'

    return size
  
  ects_without_headers_df['size'] = ects_without_headers_df['ECTS'].apply(get_size)

  print(ects_without_headers_df)



  # add semester
  def get_semester(datum):
    # datetime = parse(datum)
    date = datetime.datetime.strptime(datum, '%d.%m.%Y')
    year = date.year

    if date.month < 3:
      year -= 1

    semester = f"{year} SS"
    if date.month > 8 or date.month < 3:
      semester = f"{year}/{year+1} WS"

    return semester

  ects_without_headers_df['Semester'] = ects_without_headers_df['Datum'].apply(get_semester)

  # pd.set_option('display.max_columns', None)

  print(ects_without_headers_df)


  # Gib aus wieviele kleine und wieviele große Vorlesungen absolviert wurden
  
  number_of_rows = ects_without_headers_df[ects_without_headers_df['size'] == 'klein'].shape[0]
  print(f'The number of small courses is {number_of_rows}.')

  number_of_rows = ects_without_headers_df[ects_without_headers_df['size'] == 'groß'].shape[0]
  print(f'The number of large courses is {number_of_rows}.')
  
# wie viele VOs pro Semester habe ich gemacht? 

print ('-')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2015/2016 WS'].shape[0]
print (f'The number of courses taken in 2015 WS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2015 SS'].shape[0]
print (f'The number of courses taken in 2015 SS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2016/2017 WS'].shape[0]
print (f'The number of courses taken in 2016 WS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2016 SS'].shape[0]
print (f'The number of courses taken in 2016 SS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2017/2018 WS'].shape[0]
print (f'The number of courses taken in 2017 WS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2017 SS'].shape[0]
print (f'The number of courses taken in 2017 SS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2018/2019 WS'].shape[0]
print (f'The number of courses taken in 2018 WS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2018 SS'].shape[0]
print (f'The number of courses taken in 2018 SS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2019/2020 WS'].shape[0]
print (f'The number of courses taken in 2019 WS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2019 SS'].shape[0]
print (f'The number of courses taken in 2019 SS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2020/2021 WS'].shape[0]
print (f'The number of courses taken in 2020 WS is {number_of_rows}.')
number_of_rows = ects_without_headers_df[ects_without_headers_df['Semester'] == '2020 SS'].shape[0]
print (f'The number of courses taken in 2020 SS is {number_of_rows}.')

print('-')
semesters_df = ects_without_headers_df.groupby(['Semester']).agg({'size':'count', 'ECTS': 'sum', 'SSt.': 'sum'})
print(semesters_df)

sum_ects = sum_of_ects(semesters_df)
print(f'You have {sum_ects:.0f} ECTS in total.')


# wie viele ECTS hast du pro Semester gemacht? 

