class InsightGenerator:
    def __init__(self,data):
        self.data = data
    def generate(self):
        insights=[]
        #finance summary
        self.summary(insights)

        #finance rations
        self.ratios(insights)
        
        return insights
        
    def summary(self,insights):
        savings = self.data["total_savings"]
        income = self.data["total_income"]
        expense = self.data["total_expense"]
        average_expense = round(self.data["average_expense"],2)
        insights.append(f"Your total income : ₹ {income}")
        insights.append(f"Your total expense : ₹ {expense}")
        insights.append(f"You have Saved : {savings}")
        insights.append(f"Average expense per transaction :{average_expense}")

    def ratios(self,insights):
        savings = self.data["total_savings"]
        income = self.data["total_income"]
        expense = self.data["total_expense"]
        expense_ratio = round((expense/income)*100,2)
        savings_ratio = round((savings/income)*100,2)
        insights.append(f"You spend {expense_ratio}% of your income")
        insights.append(f"You save {savings_ratio}% of your income")