import stats
import sys
import pandas as pd


inputFile = open(sys.argv[1], 'rb')
df=pd.read_csv(inputFile)
x=stats.Stats()
x.mean(df)
x.median(df)
x.mode(df)
x.standardDev(df)
x.variance(df)
