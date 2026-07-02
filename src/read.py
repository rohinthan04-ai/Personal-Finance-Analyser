import pandas as pd

class Reader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        return pd.read_csv(self.file_path)