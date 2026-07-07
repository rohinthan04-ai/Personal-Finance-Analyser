from read import Reader
from validator import Validator
from analyser import Analyser
reader = Reader("data/transactions.csv")

df = reader.read_csv()
print(df.head())

v = Validator(df)
v.validate()

a = Analyser(df)
analysed_results = a.analyse()
print(analysed_results)


