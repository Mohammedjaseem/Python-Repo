x = 'outer x'
print (x)

def print_fn():
    global y
    y = "Inner x"
    print (y)


print_fn()
print (y)