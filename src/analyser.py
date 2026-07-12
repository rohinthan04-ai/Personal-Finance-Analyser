import pandas as pd
class Analyser:
    def __init__(self,df):
        self.df = df
    def analyse(self):
        #Calculating the total expese,income,savings
        total_expense = self.calculate_total_expense()
        total_income = self.calculate_total_income()
        total_savings = total_income-total_expense

        #Calculating the Category wise income and expense
        category_expense = self.calculate_category_expense()
        category_income = self.caluculate_category_income()

        #Calculating extremes
        highest_expense = self.calculate_highest_expense(category_expense)
        highest_income = self.calculate_highest_income(category_income)
        lowest_expense = self.calculate_lowest_expense(category_expense)
        lowest_income = self.calculate_lowest_income(category_income)
        

        #Calculating averages
        average_income = self.calculate_average_income()
        average_expense = self.calculate_average_expense()

        results = {"total_expense" : float(total_expense) ,
                   "total_income" : float(total_income) ,
                   "total_savings" : float(total_savings) ,
                   "category_expense" :  category_expense ,
                   "category_income" : category_income ,
                   "highest_expense" : highest_expense ,
                   "highest_income" : highest_income ,
                   "lowest_expense" : lowest_expense ,
                   "lowest_income" : lowest_income ,
                   "average_income" : float(average_income) ,
                   "average_expense" : float(average_expense)
                   }
        return results

    def calculate_total_expense(self):
        expense = self.df[self.df["Type"].str.lower()=="expense"]
        return expense["Amount"].sum()
    
    def calculate_total_income(self):
        income = self.df[self.df["Type"].str.lower() == "income"]
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
    
    def calculate_highest_expense(self,data):
        max=0
        result=[]
        for category,amount in data.items():
            if amount >= max:
                max = amount
        for category , amount in data.items():
            if amount == max :
                result.append(category)
        return result
    
    def calculate_highest_income(self,data):
        max=0
        result=[]
        for category,amount in data.items():
            if amount >= max:
                max = amount
        for category , amount in data.items():
            if amount == max :
                result.append(category)
        return result
    
    def calculate_lowest_income(self,data):
        min = float("inf")
        result=[]
        for category,amount in data.items():
            if amount <= min:
                min = amount
        for category , amount in data.items():
            if amount == min :
                result.append(category)
        return result
    
    def calculate_lowest_expense(self,data):
        min = float("inf")
        result=[]
        for category,amount in data.items():
            if amount <= min:
                min = amount
        for category , amount in data.items():
            if amount == min :
                result.append(category)
        return result
    
    def calculate_average_income(self):
        data = self.df[self.df["Type"].str.lower() == "income"]
        return data["Amount"].mean()
    
    def calculate_average_expense(self):
        data = self.df[self.df["Type"].str.lower() == "expense"]
        return data["Amount"].mean()