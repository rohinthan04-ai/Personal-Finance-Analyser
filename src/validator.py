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