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