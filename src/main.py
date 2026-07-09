from read import Reader
from validator import Validator
from analyser import Analyser
from visualizer import Visualizer
reader = Reader("data/transactions.csv")

df = reader.read_csv()

vali = Validator(df)
vali.validate()

anal = Analyser(df)
analysed_results = anal.analyse()

visu = Visualizer(analysed_results)
visu.visualize()