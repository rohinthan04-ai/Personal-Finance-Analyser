import matplotlib.pyplot as plt
class Visualizer:
    def __init__(self,data):
        self.data = data
    def visualize(self):
        self.expense_bar(self.data["category_expense"])

    def expense_bar(self,expense_data):
        x = expense_data.keys()
        y = expense_data.values()
        plt.bar(x,y)
        plt.title("Expense by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()