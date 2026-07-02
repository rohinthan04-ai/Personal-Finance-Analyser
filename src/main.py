import pandas as pd
from read import Reader
r = Reader("data/transactions_100.csv")
df = r.read_csv()
