monthly_income = int(input("Enter your monthly income:" ))
monthly_expenses = int(input("Enter your total monthly expenses:" ))
monthly_savings = monthly_income - monthly_expenses 
Projected_Savings = monthly_savings * 12  + monthly_savings * 12 *0.05  
print("your monthly savings is ", monthly_savings)
print("Projected Savings after one year, with interest, is: $",Projected_Savings)

