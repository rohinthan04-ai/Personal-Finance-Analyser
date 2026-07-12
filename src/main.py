from read import Reader
from validator import Validator
from analyser import Analyser
from visualizer import Visualizer
from insights import InsightGenerator
reader = Reader("data/transactions.csv")

df = reader.read_csv()

vali = Validator(df)
valid=vali.validate()
if not valid:
    print("Validation fails, program terminatd")
    exit()
anal = Analyser(df)
analysed_results = anal.analyse()

visu = Visualizer(analysed_results)
visu.visualize()

ingen = InsightGenerator(analysed_results)
insights=ingen.generate()
print(insights)