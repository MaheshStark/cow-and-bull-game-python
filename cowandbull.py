from random import randint

i=randint(1000, 9999)
j=str(i)
cows=0
bulls=0
while (1): #infinit loop
    num = input("Enter number :") # geting input to check
    for i in range(0, 4):
        if j[i] == num[i]: #check whether match or not digits
            cows = cows + 1
        else:
            bulls = bulls + 1

    print(cows ,"cows and " ,bulls ,"bulls")
    if cows==4: # check number of cows to break the while loop
        print("you won!!!")
        break
    else:
        cows=0
        bulls=0



