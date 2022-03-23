import pandas as pd
import numpy as np
df = pd.read_csv (r'C:\Users\caakh\.ssh\IS601\is601\M6\dataset1\Unity_Test_Addition.csv')
df.head()
print(df)
df.mean()
with open("Unity_Test_Addition.csv.csv") as csv_file:
    # read the csv file
    csv_reader = csv.reader(csv_file)

    # now we can use this csv files into the pandas
    df = pd.DataFrame([csv_reader], index = None)
