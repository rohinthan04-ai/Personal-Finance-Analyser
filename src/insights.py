class InsightGenerator:
    def __init__(self,data):
        self.data = data
    def generate(self):
        insights=[]
        insights.append(self.savings())

        return insights
        
    def savings(self):
        savings = self.data["total_savings"]
        return "You have Saved ₹{}".format(savings)
