# https://pandas.pydata.org/about/index.html
# https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
# http://pandas.pydata.org

import numpy as np
import pandas as pd

if __name__ == "__main__":
    data_df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [3, 2, 1],
    })
    print('-')
    print('data_df')
    print(data_df)
    
    series = pd.Series([5, 6, 7])
    print('-')
    print('series')
    print(series)

    data1_df = data_df[1:3]
    print('-')
    print('data1_df')
    print(type(data1_df))
    print(data1_df)

    data2_series = data_df['A']
    print('-')
    print('data2_series')
    print(type(data2_series))
    print(data2_series)

    sum = data2_series.sum()
    print(sum)
    
    # dataframe: https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
    # max: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.max.html
    # median
    # min
    # average
    # sum of strings? 

