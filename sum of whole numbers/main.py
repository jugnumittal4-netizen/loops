print("-------------------Hi Welcome To sum of whole numbers Program--------------------")
n = int(input("enter a whole number which's sum you want to find: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
    print("the sum of whole numbers from 1 to", n, "is:", sum)