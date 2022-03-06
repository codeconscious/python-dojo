print('Hello 世界! ' * 3)

myList = [10 ** 3, 20, 30] # Two asterisks represents powers
myList.append(1)
myList.append(2)
myList.append(3)
myOtherList = [-3, 4] * 10 # You can repeat list contents too.
finalList = myList + myOtherList

sum = 0
for x in finalList:
    sum += x
avg = sum / len(finalList)
print("The total is %s, and the average is %s" % (str(sum), str(avg)))