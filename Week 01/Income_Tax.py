'''
Income tax is calculated as per the following table 
Annual Income
Tax percentage
Up to 2.5 Lakhs 
No Tax
Above 2.5 Lakhs to 5 Lakhs
5%
Above 5 Lakhs to 10 Lakhs
20%
Above 10 Lakhs to 50 Lakhs
30%



'''
def tax_calculator(income):
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = income * 0.05
    elif income <= 1000000:
        tax = income * 0.20
    elif income <= 5000000:
        tax = income * 0.3

    print("Income Tax Amount : ",tax,"\n")
    return tax

income = int(float((input("\nEnter your income: "))))
tax_calculator(income)