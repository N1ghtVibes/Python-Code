cookies=1
click=1
Dirtclicker=100
Dirtclickeramt=0
Dirtclickerpwr=3

while 1==1:
    command=input("What is your command? ")
    if command=='c':
        cookies=cookies+click
        print("You have: ",cookies,"cookies ")
    if command=='exit':
        print("Yes?")
        print("No? ")
        usure=input("Are you sure you want to exit? ")
        if usure=="No":
            print("Ok")
        if usure=="Yes":
            exit()
    if command=='shop':
        print("")
        print("Dirtclicker: Increases clicking power by 2: Cost: ",Dirtclicker, "cookies")
        print("")
        print("Woodenclicker: Increases clicking power to 4: Cost: 100 cookies")
        buy=input("What do you want to buy? ")
        if buy=='Dirtclicker':
            if cookies<Dirtclicker:
                print("You can't buy the Dirtclicker")
            if cookies>=Dirtclicker:
                print("You bought Dirtclicker")
                Dirtclickeramt+1
                click=Dirtclickerpwr
                cookies-Dirtclicker
            else:
                print("That's not a item")
