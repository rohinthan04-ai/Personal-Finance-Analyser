class InsightGenerator:
    def __init__(self,data):
        self.data = data
    def generate(self):
        insights=[]
        #finance summary
        self.summary(insights)

        #finance rations
        self.ratios(insights)
        
        #category wise insights
        self.category_analysis(insights)
        
        #health insights
        self.health(insights)
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

    def category_analysis(self,insights):
        highest_expense=self.data["highest_expense"]
        lowest_expense=self.data["lowest_expense"]
        highest_income=self.data["highest_income"]
        lowest_income=self.data["lowest_income"]
        highest_expense_category = " ".join(highest_expense)
        lowest_expense_category =' '.join(lowest_expense)
        highest_income_category = ' '.join(highest_income)
        lowest_income_category =' '.join(lowest_income)
        
        insights.append(f"{highest_expense_category} is your biggest spending category")
        insights.append(f"{lowest_expense_category} is your least spending category")
        insights.append(f"{highest_income_category} is your Primary Source of income")
        insights.append(f"{lowest_income_category} is your smallest source of income.")

    def health(self,insights):
        savings = self.data["total_savings"]
        income = self.data["total_income"]
        expense = self.data["total_expense"]
        savings_ratio = round((savings/income)*100,2)
        expense_ratio = round((expense/income)*100,2)
        if(expense<income):
            insights.append("Your expense are within your income")
        elif expense == income :
            insights.append("⚠ Your income and expenses are equal. You are not saving any money.")
        else :
            insights.append("⚠ You are spending more than you earn.")

        if savings_ratio > 30:
            insights.append(f"Excellent savings rate ({savings_ratio}%)")
        elif savings_ratio < 30 and savings_ratio > 10 :
            insights.append(f"Your savings rate is healthy ({savings_ratio}%)")
        else:
            insights.append(f"⚠ Your savings rate is low.({savings_ratio}%)")

        if expense_ratio < 70 :
            insights.append("Your spending is well under control.")
        elif expense_ratio > 70 and expense_ratio <90 :
            insights.append("Most of your income goes toward expenses.")
        else :
            insights.append("⚠ Your expenses consume almost all of your income.")

        if income > expense and savings_ratio >20 :
            insights.append("Overall, your financial position looks healthy.")
        elif expense >income :
            insights.append("⚠ Your current financial position needs attention.")
        