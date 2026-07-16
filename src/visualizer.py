import matplotlib.pyplot as plt
class Visualizer:
    def __init__(self,data):
        self.data = data
    def visualize(self):
        self.expense_bar(self.data["category_expense"])
        self.income_bar(self.data["category_income"])
        self.expense_income_savings_bar(self.data["total_expense"],self.data["total_income"],self.data["total_savings"])
    def expense_bar(self,expense_data):
        fig,ax = plt.subplots()
        x = expense_data.keys()
        y = expense_data.values()
        ax.bar(x,y)
        ax.set_title("Expense by Category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Amount")
        ax.tick_params(axis="x", rotation=45)
        fig.tight_layout()
        return fig
    def income_bar(self,income_data):
        fig,ax = plt.subplots()
        x = income_data.keys()
        y = income_data.values()
        ax.bar(x,y)
        ax.set_title("Income by category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Amount")
        ax.tick_params(axis="x", rotation=45)
        fig.tight_layout()
        return fig
    def expense_income_savings_bar(self,expense_data,income_data,savings):
        fig,ax=plt.subplots()
        x = ["Savings","Expense","Income"]
        y = [savings,expense_data,income_data]
        ax.barh(x,y)
        ax.set_title("Income VS Expense VS Savings")
        ax.set_xlabel("Amount")
        ax.set_ylabel("Category")
        
        fig.tight_layout()
        return fig