from read import Reader
from validator import Validator
from analyser import Analyser
from visualizer import Visualizer
from insights import InsightGenerator
def main():
    #-----READING A FILE USING READER MODULE-----
    reader = Reader("data/transactions.csv")
    transactions = reader.read_csv()

    #--------VALIDATING THE GIVEN FILE USING THE VALIDATOR MODULE-------
    validator = Validator(transactions)
    is_valid=validator.validate()
    if is_valid != True:
       print(is_valid)
       return

    #-----ANALYSING THE DATA USING THE ANALYSER MODULE----
    analyser = Analyser(transactions)
    analysed_results = analyser.analyse()

    #-----VISUALIZING THE ANALYSED DATA USING THE VISUALIZER MODULE-----
    visualyser = Visualizer(analysed_results)
    visualyser.visualize()

    #-----GENERATING THE INSIGHTS FOR THE TRANSACTIONS FROM THE ANALYSED DATA-----
    insight_generator = InsightGenerator(analysed_results)
    insights=insight_generator.generate()


if __name__ =="__main__":
    main()