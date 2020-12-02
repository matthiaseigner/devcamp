import pandas as pd
import numpy as np

def sum_of_ects(courses_df):
    sum_ects = courses_df['ECTS'].sum()
    return sum_ects
    
if __name__ == "__main__": 
    ects_df = pd.read_csv('ects.csv')

    # print sum of ects
    sum_ects = sum_of_ects(ects_df)
    print(f'You have {sum_ects:.0f} ects in total')

    # pring ects of semesters

    