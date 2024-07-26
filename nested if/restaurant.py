print("SELECT YOUR CHOICE WITH NUMBERS.😊")
print("1=waffle hut...")
print("2=banana leaf...")
print("3=chillies....")
a=int(input("Choose your favourite restaurant="))
if a==1:
    print("waffle Hut")
    print("1=milk shake")
    print("2=Waffles")
    print("3=ice cream waffles")
    median=int(input("choose your median: "))
    if median==1:
        print("milk shake....❤️")
        print("1=choco shake,$20")
        print("2=nutty shake,$20✨")
        milkshake=int(input("Select your milkshake:= "))
        if milkshake==1:
            print("your milkshake is:= choco shake")
            print("The price is= $20")
            addd=input("Do u want ADDon yes or no??:=")
            if addd=='yes':    
                print("the add on are:= \ncaramel  \nnuts ")
                p1=20
                add=input("enter your add on:= ")
                if add=='caramel':
                    print("your addon is caramel ")
                    price=p1+20
                    print("Total price is :=",price)
                elif add=='nuts':
                    print("your addon is nuts ")
                    price=p1+30
                    print("Total price is :=",price)
                else:
                    print("INVALID SELECTION")
            elif addd=='no':
                print("Total price is= $20")
            else:
                print("INVALID SELECTION...")        
        elif milkshake==2:
            print("your milkshake is:= nutty shake")
            print("The price is= $20")
            addd=input("Do u want ADDon yes or no??:=")
            if addd=='yes':    
                print("the add on are:= \ncaramel  \nnuts ")
                p1=20
                add=input("enter your add on:= ")
                if add=='caramel':
                    print("your addon is caramel ")
                    price=p1+20
                    print("Total price is :=",price)
                elif add=='nuts':
                    print("your addon is nuts ")
                    price=p1+30
                    print("Total price is :=",price)
                else:
                    print("INVALID SELECTION")
            elif addd=='no':
                print("Total price is= $20")
            else:
                print("INVALID SELECTION...")
        else:
            print("INVALID SELECTION")
    elif median==2:
        print("waffles....❤️")
        print("1=death by choco,$20")
        print("2=vannila✨,$20")
        waffle=int(input("Select your waffle:="))
        if waffle==1:
            print("your waffle is := Death by choco")
            print("The price is= $20")
        elif waffle==2:
            print("your waffle is:= vannila")
            print("The price is= $20")
        else:
            print("INVALID SELECTION")
    elif median==3:
        print("ice cream waffles...❤️")
        print("1=choco waffles with vannilla ice cream,$20")
        print("2=choco waffles with chocolate ice cream,$20")
        icecream_waffle=int(input("Select your ice cream_waffles:="))
        if icecream_waffle==1:
            print("your waffle is := choco waffles with vannilla ice cream")
            print("The price is= $20")
        elif icecream_waffle==2:
            print("your waffle is:= choco waffles with chocolate ice cream")
            print("The price is= $20")
        else:
            print("INVALID SELECTION")
    else:
            print("INVALID SELECTION")
elif a==2:
    print("RESTAURANT: banana leaf")
    print("1=starters")
    print("2=main course")
    print("3=desert")
    median=int(input("choose your median: "))
    if median==1:
        print("starters....❤️")
        print("1=chicken  lolipop,$20")
        print("2=chicken soup✨,$20")
        starter=int(input("Select your Starter;="))
        if starter==1:
            print("YOUR STARTER IS : chicken lolipop")
            print("The price is= $20")
        elif starter==2:
            print("YOUR STARTER IS : chicken soup.")
            print("The price is= $20")
        else:
            print("INVALID SELECTION")
    elif median==2:
        print("main course....❤️")
        print("1=chicken biriyani,$20")
        print("2=veg biriyani✨,$20")
        main_course=int(input("select your main course:= "))
        if main_course==1:
            print("YOUR main_course IS : chicken biriyani")
            print("The price is= $20")
        elif main_course==2:
            print("YOUR main_course IS : veg biriyani.")
            print("The price is= $20")
        else:
            print("INVALID SELECTION")
    elif median==3:
        print("Desert....❤️")
        print("1=ice cream,$20")
        print("2=milk shake,$20")
        desert=int(input("select your desert:= "))
        if desert==1:
            print("YOUR DESERT IS : ice cream")
            print("The price is= $20")
        elif desert==2:
            print("YOUR DESERT IS : milk shake.")
            print("The price is= $20")
        else:
            print("INVALID SELECTION")
    else:
            print("INVALID SELECTION")
elif a==3:
    print("RESTAURANT: chillies..")
    print("1=starters")
    print("2=main course")
    print("3=desert")
    median=int(input("choose your median: "))
    if median==1:
        print("starters....❤️")
        print("1=chicken  lolipop,$20")
        print("2=chicken soup✨,$20")
        starter=int(input("Select your Starter;="))
        if starter==1:
            print("YOUR STARTER IS : chicken lolipop")
            print("The price is= $20")
        elif starter==2:
            print("YOUR STARTER IS : chicken soup.")
            print("The price is= $20")
        else:
            print("INVALID SELECTION")
    elif median==2:
        print("main course....❤️")
        print("1=chicken biriyani,$20")
        print("2=veg biriyani✨,$20")
        main_course=int(input("Select your main_course="))
        if main_course==1:
            print("YOUR MAIN COURSE IS : chicken Biriyani")
            print("The price is= $20")
        elif main_course==2:
            print("YOUR MAIN COURSE IS : veg Biriyani.")
            print("The price is= $20")
        else:
            print("INVALID SELECTION")
    elif median==3:
        print("Desert....❤️")
        print("1=ice cream,$20")
        print("2=milk shake,$20")
        desert=int(input("select your desert:= "))
        if desert==1:
            print("YOUR DESERT IS : ice cream")
            print("The price is= $20")
        elif desert==2:
            print("YOUR DESERT IS : milk shake.")
            print("The price is= $20")
        else:
            print("INVALID SELECTION")
    else:
            print("INVALID SELECTION")
else:
    print("INVALID SELECTION")