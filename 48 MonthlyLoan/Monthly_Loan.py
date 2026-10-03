def Loan(LoanAmount,ManyMonths):
    MonthlyPayment = round(LoanAmount / ManyMonths)
    return str(MonthlyPayment) + ' Dollar per month'

LoanAmount = float(input("Enter LoanAmount: "))
ManyMonths = float(input("Enter how many months do you need to settle the Loan: "))

print(Loan(LoanAmount,ManyMonths))

