import pandas as pd
class Analyser:
    def __init__(self,df):
        self.df = df
    def analyse(self):
        #Calculating the total expese,income,savings
        total_expense = self.calculate_total_expense(self.df[self.df["Type"].str.lower()=="expense"])
        total_income = self.calculate_total_income(self.df[self.df["Type"].str.lower() == "income"])
        total_savings = total_income-total_expense
        print(total_income)
        print(total_expense)
        print(total_savings)

        #Calculating the Category wise income and expense
        category_expense = self.calculate_category_expense()
        category_income = self.caluculate_category_income()
        highest_expense = self.calculate_highest_expense()
        print(highest_expense)
        print(category_expense)
        print(category_income)


    def calculate_total_expense(self,expense):
        return expense["Amount"].sum()
    
    def calculate_total_income(self,income):
        return income["Amount"].sum()
    
    def calculate_category_expense(self):
        data = self.df[self.df["Type"].str.lower()=="expense"]
        g = data.groupby(["Category"])
        result = g["Amount"].sum()
        result = result.to_dict()
        return result
    def caluculate_category_income(self):
        data = self.df[self.df["Type"].str.lower() == "income"]
        g = data.groupby('Category')
        result = g["Amount"].sum()
        result = result.to_dict()
        return result
    
    def calculate_highest_expense(self):
        data = self.df[self.df["Type"].str.lower() == "expense"]
        result = data[data["Amount"] == data["Amount"].max()]
        result = result.to_dict(orient='records')
        return result