income = int(input("Enter your monthly income:" ))
expenses = int(input("Enter your total monthly expenses:" ))
monthly_savings = income - expenses 
Projected_Savings = monthly_savings * 12  + monthly_savings * 12 *0.05  
print("your monthly savings is ", monthly_savings)
print("Projected Savings after one year, with interest, is: $",Projected_Savings)

