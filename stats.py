import pandas as pd


class Stats:

    def mean(self,df):
        print("MEAN")
        print(df.mean())

    def median(self,df):
        print("MEDIAN")
        print(df.median())

    def mode(self,df):
        print("MODE")
        print(df.mode())

    def standardDev(self,df):
        print("STANDARD DEVIATION")
        print(df.std())

    def variance(self,df):
        print("VARIANCE")
        print(df.var())




