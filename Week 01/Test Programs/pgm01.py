points = 174  # use this input to make your submission

if (points < 51 ):
    prize="wooden rabbit"

elif ( points < 151):
    prize="no prize"
    
elif ( points < 181):
    prize="wafer-thin mint"
    
elif ( points < 201):
    prize="penguin"

else:
    print("Invalid Input!")


print("Congratulations! You won a {}!".format(prize))