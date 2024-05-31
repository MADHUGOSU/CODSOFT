import random
while 1:
    userchoi=int(input("enter your choice:\n0 for ROCK,\n1 for SCISSORS,\n2 for PAPER\n3 for exit\n"))
    if userchoi >3 or userchoi <0:
        print("INVALID INPUT, YOU LOSE THE GAME")
    elif(userchoi == 3):
        break;
    else:
        compchoi=random.randint(0,2)
        print("computer chose:")
        print(compchoi)
        if compchoi == userchoi:
            print("DRAW THE GAME")
        elif compchoi > userchoi:
            print("YOU LOSE THE GAME")
        elif compchoi < userchoi:
            print("YOU WIN THE GAME")
        elif compchoi ==0 and userchoi ==2:
            print("YOU LOSE THE GAME")
        elif compchoi ==2 and userchoi ==0:
            print("YOU WIN THE GAME")
    

    
