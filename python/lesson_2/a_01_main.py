import pandas as pd
import numpy as np

# analyze data for students from 
# https://data.europa.eu/euodp/en/data/dataset/2nd-survey-of-schools-ict-in-education

students_file = './data/ICT_Students.csv'
students_lab_file = './data/ICT_Students_lab.csv'

if __name__ == "__main__": 
    students_df = pd.read_csv(students_file)

    # Question ST05
    # "How often do you take part in the following activities in your free time, 
    # at home or any place other than school?<br/><br/><i>Please select one answer for each item.</i>"
    #
    # Answer: ST05:Q03
    # Column: ST05Q03
    # "Reading and watching the news online"
    values = {
        1: "Never or almost never",
        2: "Several times a month",
        3: "At least once a week",
        4: "Every day or almost every day",
        999: "Don’t know/Prefer not to say",
    }
    
    # print(students_df[students_df['ST05Q03'] == '999'])

    # clean
    students_df = students_df[(students_df['ST05Q03'] !=  ' ') & (students_df['ST05Q03'] != '999')]
    students_df['ST05Q03'] = students_df['ST05Q03'].astype(int)

    students_st05_df = students_df.groupby(['COUNTRY']).agg({'ST05Q03': 'mean'})
    print(len(students_df))
    print( students_st05_df.sort_values(by='ST05Q03'))