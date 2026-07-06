import pandas as pd
class Analyser:
    def __init__(self,df):
        self.df = df
    def analyse(self):
        #Calculating the total expese,income,savings
        total_expense = self.calculate_total_expense(self.df[self.df["Type"].str.lower()=="expense"])
        total_income = self.calculate_total_income(self.df[self.df["Type"].str.lower() == "income"])
        print(total_income)
        print(total_expense)

    def calculate_total_expense(self,expense):
        return expense["Amount"].sum()
    
    def calculate_total_income(self,income):
        return income["Amount"].sum()