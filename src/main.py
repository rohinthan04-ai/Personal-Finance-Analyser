from read import Reader
from validator import Validator
reader = Reader("data/transactions.csv")

df = reader.read_csv()
print(df.head())

v = Validator(df)
v.validate()


