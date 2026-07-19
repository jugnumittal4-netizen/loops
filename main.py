print("-------------------Hi Welcome To Reverse order Program--------------------")
n = int(input("enter a whole number which's reverse order you want to find: "))
print("numbers from{0} to {1} are".format( n , 1 ))
for i in range (n, 0, -1):
    print(i)
