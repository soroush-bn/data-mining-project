import pandas as pd
import os


def merge_into_one(self, path):
    cwd = os.path.abspath(path)
    files = os.listdir(cwd)
    df = pd.DataFrame()
    for file in files:
        if file.endswith('.xls'):
            df = df.append(pd.read_excel(os.path.join(cwd, file)), ignore_index=True)
    df.head()
    df.to_excel('results.xlsx')
    print("merged")