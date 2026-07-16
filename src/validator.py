import pandas as pd
from datetime import datetime

class Validator:
    def __init__(self,transactions):
        self.transactions = transactions

    def validate(self):
        #cheacking the heading
        if not self.validate_field():
            return "Invalid Feild"

        #cheacking the date
        for index,date in self.transactions.iterrows():
            if not self.validate_date(date["Date"]):
                return (f"Invalid date : '{date["Date"]}' in row {index+1}")
        
        #checking type
        for index,type_ in self.transactions.iterrows():
            if not self.validate_type(type_["Type"].lower()):
                return (f"Invalid type : '{type_["Type"]}' in row {index+1}")
            
        #checking category
        for index,category in self.transactions.iterrows():
            if not self.validate_category(category["Category"].lower()):
                return (f"Invalid category : '{category["Category"]}' in row {index+1}")
        
        #validating the amount
        for index,amount in self.transactions.iterrows():
            if not self.validate_amount(amount["Amount"]):
               return(f"Invalid Amount : '{amount["Amount"]}' in row {index+1}")
            
        #validating description
        for index,string in self.transactions.iterrows():
            if not self.validate_description(string["Description"]):
                return(f"Invalid Description in row : {index+1}")
            
        #validating the category and type
        for index,row in self.transactions.iterrows() :
            if not self.validate_type_category(row["Type"].lower(),row["Category"].lower()):
                return(f"Type and Category Mismatch. 'Type: {row["Type"]} and Category: {row["Category"]}' in row {index+1}")
            
        return(True)
        
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