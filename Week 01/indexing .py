items=['bananas','mattresses','dog kennels','machine','cheeses']
print("\nPrint using zip function: \n")
for i, item in zip(range(len(items)),items):
    print(i,item)


# or enumarate function can be used to get the index of the item
print("\nPrint using enumarate function: \n")
for i, item in enumerate(items):
    print(i,item)
