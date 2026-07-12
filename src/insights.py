class InsightGenerator:
    def __init__(self,data):
        self.data = data
    def generate(self):
        insights=[]
        #finance summary
        self.summary(insights)

        
        
        return insights
        
    def summary(self,insights):
        savings = self.data["total_savings"]
        income = self.data["total_income"]
        expense = self.data["total_expense"]
        average_expense = self.data["average_expense"]
        insights.append(f"Your total income : ₹ {income}")
        insights.append(f"Your total expense : ₹ {expense}")
        insights.append(f"You have Saved : {savings}")
        insights.append(f"Average expense per transaction :{average_expense}")
   