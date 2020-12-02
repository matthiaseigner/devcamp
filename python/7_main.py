import pandas as pd
import numpy as np

def sum_of_ects(courses_df):
    sum_ects = courses_df['ECTS'].sum()
    return sum_ects

def sum_of_sst(courses_df):
    sum_sst = courses_df['SSt.'].sum()
    return sum_sst
    
if __name__ == "__main__": 
    ects_df = pd.read_csv('ects.csv')

    # print sum of ects
    sum_ects = sum_of_ects(ects_df)
    print(f'You have {sum_ects:.0f} ECTS in total.')

    # print ects of semesters
    # fehlt

    # print sum of SSt. 
    sum_sst = sum_of_sst(ects_df)
    print(f'You have {sum_sst:.0f} semester hours in total.')

    # print spacer
    print('-')

    # print average of ects
    number_of_rows = ects_df.shape[0]-1
    print(f'The number of classes, in which {sum_ects:.0f} ects have been acquired, is {number_of_rows:.0f}.')
    average_ects = sum_ects/number_of_rows
    print(f'On average you have acquired {average_ects:.2f} ects per class.')
    


    