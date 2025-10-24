import random
RandomNumber =random.randrange(1,100)
userInput=int(input("Enter the number:"))

if userInput > RandomNumber :
    print(RandomNumber)
    print("The number is high")
elif RandomNumber >userInput:
    print(RandomNumber)
    print("The number is low")
else:
    print(RandomNumber)
    print("The number is match")
