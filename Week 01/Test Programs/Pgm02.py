while True:
    answer = int(input("Enter the Number: "))
    guess = int(input("Guess the Number: "))
    
    if (answer > guess):
        result = "Oops!  Your guess was too low."
    elif (answer < guess):
        result = "Oops!  Your guess was too high."
    elif (answer == guess):
        result = "Nice!  Your guess matched the answer!"
    print(result)