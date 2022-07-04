"""
1 

2 3 

4 5 6 

7 8 9 10 

etc.......

"""

limit = int(input("Enter the limit: "))
print_num = 1
for i in range(1,limit+1):
    for j in range(1,i+1):
        if print_num <= limit:
            print(print_num,end=" ")
            print_num += 1
        else:
            break
    print("\n")