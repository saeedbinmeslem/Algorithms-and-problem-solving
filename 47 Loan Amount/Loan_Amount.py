def Loan(LoanAmount,MonthlyPayment):
    ManyMonths = int(LoanAmount / MonthlyPayment)
    return str(ManyMonths) + ' Months'

LoanAmount = float(input("Enter LoanAmount: "))
MonthlyPayment = float(input("Enter MonthlyPayment: "))

print(Loan(LoanAmount,MonthlyPayment))

