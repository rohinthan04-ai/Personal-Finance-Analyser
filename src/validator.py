import pandas as pd
class Validator:
    def __init__(self,transactions):
        self.transactions = transactions

    def validate(self):
        self.validate_field()

    def validate_field(self):
        heading = set(self.transactions.columns.str.lower())
        if heading == {'amount', 'category', 'description', 'date', 'type'} :
            return
        else:
            print("The provided heading is invalid")
