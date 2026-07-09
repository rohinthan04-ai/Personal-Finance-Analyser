import matplotlib.pyplot as plt
class Visualizer:
    def __init__(self,data):
        self.data = data
    def visualize(self):
        self.expense_bar(self.data["category_expense"])
        self.income_bar(self.data["category_income"])
        self.expense_income_savings_bar(self.data["total_expense"],self.data["total_income"],self.data["total_savings"])
    def expense_bar(self,expense_data):
        x = expense_data.keys()
        y = expense_data.values()
        plt.bar(x,y)
        plt.title("Expense by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()
    def income_bar(self,income_data):
        x = income_data.keys()
        y = income_data.values()
        plt.bar(x,y)
        plt.title("Income by category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()
    def expense_income_savings_bar(self,expense_data,income_data,savaings):
        x = ["Savings","Expense","Income"]
        y = [savaings,expense_data,income_data]
        plt.barh(x,y)
        plt.show()