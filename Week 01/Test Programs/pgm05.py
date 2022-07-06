names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for i in range(len(names)):
    names[i]=names[i].replace(" ","_")
    usernames.append(names[i].lower())

print(usernames)