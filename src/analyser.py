import pandas as pd
class Analyser:
    def __init__(self,df):
        self.df = df
    def analyse(self):
        #Calculating the total expese
        total_expense = self.calculate_total_expense(self.df[self.df["Type"].str.lower()=="expense"])
        print(total_expense)

    def calculate_total_expense(self,expense):
        return expense["Amount"].sum()