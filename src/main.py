from read import Reader

reader = Reader("data/transactions.csv")

df = reader.read_csv()

print(df)
