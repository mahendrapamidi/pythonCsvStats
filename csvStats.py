import csv
import sys
import pandas as pd

inputFile = open(sys.argv[1], 'rb')
df=pd.read_csv(inputFile)
z=df.values.tolist()
print(z)

