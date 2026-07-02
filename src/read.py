import pandas as pd
class Reader:
    def __init__(self,path):
        self.path = path
    def read_csv (self):
        return pd.read_csv(self.path)
    