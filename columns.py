import pandas as pd 

def col(df):
    for i in df.columns:
        print(df[i].value_counts)
        print()