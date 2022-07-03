#Program should accept 3 inputs from the user and calculate simple interest for the given inputs. Formula: SI=(P*R*n)/100)

Principal_Amount = int(input("Enter the Principal Amount: "))
Rate_of_Interest = float(input("Enter the Rate of Interest: "))
Time_in_Years = int(input("Enter the Time in Years: "))
Simple_Interest = ( Principal_Amount * Rate_of_Interest * Time_in_Years ) / 100
print("The Simple Interest is: ", Simple_Interest)