import pandas as pd
from datetime import datetime

class Validator:
    def __init__(self,transactions):
        self.transactions = transactions

    def validate(self):
        #cheacking the heading
        if not self.validate_field():
            return False

        #cheacking the date
        for date in self.transactions["Date"]:
            if not self.validate_date(date):
                print("Invalid date",date)
                return False
        
        #checking type
        for type_ in self.transactions["Type"].str.lower():
            if not self.validate_type(type_):
                print("Invalid type",type_)
                return False
            
        #checking category
        for category in self.transactions["Category"].str.lower():
            if not self.validate_category(category):
                print("Invalid category",category)
                return False
        
        #validating the amount
        for amount in self.transactions["Amount"]:
            if not self.validate_amount(amount):
                print("Invalid amount ",amount)
                return False
            
        #validating description
        for string in self.transactions["Description"]:
            if not self.validate_description(string):
                print("Invalid description",string)
                return False
            
        #validating the category and type
        for index,row in self.transactions.iterrows() :
            if not self.validate_type_category(row["Type"].lower(),row["Category"].lower()):
                print("Error in row :",index+1)
                print("Type and Category Mismatch. Type: ",row["Type"],"Category: ",row["Category"])
                return False
            
        return True
        
    def validate_field(self):
        heading = set(self.transactions.columns.str.lower())
        if heading == {'amount', 'category', 'description', 'date', 'type'} :
            return True
        else:
            print("The provided heading is invalid")
            return False

    def validate_date(self,date):
        try:
            datetime.strptime(date,"%Y-%m-%d")
            return True
        except ValueError:
            return False
        
    def validate_type(self,type_):
        if type_ in {"income","expense"} :
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
        
    def validate_type_category(self,type_,category):
        if type_ == "expense" :
            return category in {"entertainment","food","transport","shopping","bills","healthcare","education"}
        else:
            return category not in {"entertainment","food","transport","shopping","bills","healthcare","education"}