intro = 'Hello 世界'
print(intro)
print(intro[0:5]) # The colon can be omitted
print(intro[0::2]) # Third number is the step
print(intro[::-1]) # Reverse like this
print((intro + " ") * 3)

words = intro.split(" ")
print("There are %d words in '%s'" % (len(words), intro))

if words[0] == 'Hello' and words[1] == '世界': # Use "and"
    print("Looks good!")
elif words[0] == "Goodbye":
    print("Hmm...")
else:
    print("Failure!")

if "世界" in words: # Contains
    print("Yes!")
else:
    print("Sorry, no...")

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
print("The total is %d, and the average is %f." % (sum, avg))

for n in range(5, 10):
    print(n)

# While loops can have else!
count = 0
while (count < 4): # Prints 0 to 3
    print(count)
    count += 1
else: # This is not hit if "break" is used
    print("All done!")

# Object equality check
if myList is finalList:
    print("One and them same instance")
else:
    print("Not the same instance")