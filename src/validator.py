import pandas as pd
from datetime import datetime

class Validator:
    def __init__(self,transactions):
        self.transactions = transactions

    def validate(self):
        #cheacking the heading
        self.validate_field()

        #cheacking the date
        for date in self.transactions["Date"]:
            if not self.validate_date(date):
                print("Invalid date",date)
                return
        
        #checking type
        for type in self.transactions["Type"].str.lower():
            if not self.validate_type(type):
                print("Invalid type",type)
                return
            
        #checking category
        for category in self.transactions["Category"].str.lower():
            if not self.validate_category(category):
                print("Invalid category",category)
                return
        
        #validating the amount
        for amount in self.transactions["Amount"]:
            if not self.validate_amount(amount):
                print("Invalid amount ",amount)
                return
            
        #validating description
        for string in self.transactions["Description"]:
            if not self.validate_description(string):
                print("Invalid description",string)
                return
            
        #validating the category and type
        for index,row in self.transactions.iterrows() :
            if not self.validate_type_category(row["Type"].lower(),row["Category"].lower()):
                print("Error in row :",index+1)
                print("Type and Category Mismatch. Type: ",row["Type"],"Category: ",row["Category"])
        
    def validate_field(self):
        heading = set(self.transactions.columns.str.lower())
        if heading == {'amount', 'category', 'description', 'date', 'type'} :
            return
        else:
            print("The provided heading is invalid")

    def validate_date(self,date):
        try:
            datetime.strptime(date,"%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    def validate_type(self,type):
        if type in {"income","expense"} :
            return True
        else:
            return False
        
    def validate_category(self,category):
        if category in {"salary", "freelance","entertainment","investment","gift","food","transport","shopping","bills","healthcare","education","business"} :
            return True
        else:
            return False
    def validate_amount(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            return False
        return amount > 0
    
    def validate_description(self,string):
        if pd.isna(string):
            return False
        return set(string) != {" "}
        
    def validate_type_category(self,type,category):
        if type == "expense" :
            return category in {"entertainment","food","transport","shopping","bills","healthcare","education"}
        else:
            return category not in {"entertainment","food","transport","shopping","bills","healthcare","education"}