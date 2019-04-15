import pandas as pd
from pandas.api.types import is_string_dtype

df = pd.read_csv("train.csv")
df.head()

dfRevCols = df[df.columns[::-1]]
dfRevCols.head()

dfEveryOtherCol = df[df.columns[::2]]
dfEveryOtherCol.head()

dfEveryThirdRev = df[df.columns[::3]]
dfEveryThirdRev.head()

def rev(string):
    return string[::-1]

strCols = [col for col in dfEveryThirdRev.columns 
                    if is_string_dtype(dfEveryThirdRev[col])]

for col in strCols:
    dfEveryThirdRev.loc[:,col] = dfEveryThirdRev[col].map(rev)

print(dfEveryThirdRev.head())