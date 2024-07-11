import random
list=["1","2","3"]
try:
    def is_winner(x,y):
        if x==y:
            return("Draw")
        elif x=="1" and y=="2":
            return("Lose")
        elif x=="1" and y=="3":
            return("Win")
        elif x=="2" and y=="1":
            return("Win")
        elif x=="2" and y=="3":
            return("Lose")
        elif x=="3" and y=="1":
            return("Lose")
        elif x=="3" and y=="2":
            return("Win")
        else:
            print("Error out of Range Choice!")

    def is_loser(x,y):
        if x==y:
            return("Draw")
        elif x=="1" and y=="2":
            return("Win")
        elif x=="1" and y=="3":
            return("Lose")
        elif x=="2" and y=="1":
            return("Lose")
        elif x=="2" and y=="3":
            return("Win")
        elif x=="3" and y=="1":
            return("Win")
        elif x=="3" and y=="2":
            return("Lose")
        else:
            print("Error out of Range Choice!")

    def translate_by_num(x):
        if x==1 or x=="1":
            return "Rock"
        elif x==2 or x=="2":
            return "Paper"
        elif x==3 or x=="3":
            return "Scissor"

    print("\nWelcome To Rock Paper Scissor Game By (Yassin Bassam)\n")
    while True:
        no_wins=0
        no_loses=0
        no_draws=0
        no_wins_p2=0
        no_loses_p2=0
        no_draws_p2=0
        print("Menu:\n1)VS Computer\n2)2 Players\n3)Exit\n")
        i1=input("Enter number from 1 to 3:")
        
        while i1 != "1" and i1 != "2" and i1 != "3":
            print("\nPlease enter Valid number!\n")
            print("Menu:\n1)VS Computer\n2)2 Players\n3)Exit\n")
            i1=input("Enter number from 1 to3:")

        if i1=="1":
            while True:
                print("Your Turn:\n1)Rock\n2)Paper\n3)Scissor\n")
                i2=input("Enter your choice:")
                while i2!="1" and i2!="2" and i2!="3":
                    print("\nPlease enter Valid number!\n")
                    print("Your Turn:\n1)Rock\n2)Paper\n3)Scissor\n")
                    i2=input("Enter your choice:")
                computer_choice=random.choice(list)
                print(f"\nYou choose {translate_by_num(i2)} and Computer Choose {translate_by_num(computer_choice)}")
                print("You",is_winner(i2,computer_choice),"\n")
                if is_winner(i2,computer_choice)=="Win":
                    no_wins+=1
                elif is_winner(i2,computer_choice)=="Lose":
                    no_loses+=1
                elif is_winner(i2,computer_choice)=="Draw":
                    no_draws+=1
                else:
                    print("Error in Score!")
                i3=input("Do you want to play again?\n1)Yes\n2)No\n")
                while i3!="1" and i3!="2":
                    print("\nPlease enter Valid number!\n")
                    i3=input("Do you want to play again?\n1)Yes\n2)No\n")
                if i3=="1":
                    print("Let's Play again\n")
                elif i3=="2":
                    print(f"\nScore:\n{no_wins} Wins  {no_draws} Draws  {no_loses} Loses\n")
                    print("Back to ",end="")
                    break
                else:
                    print("I will never show LoL")
        elif i1=="2":
            while True:
                print("\nPlayer1 Turn:\n1)Rock\n2)Paper\n3)Scissor\n")
                i2=input("Enter your choice:")
                while i2!="1" and i2!="2" and i2!="3":
                    print("\nPlease enter Valid number!\n")
                    print("\nPlayer1 Turn:\n1)Rock\n2)Paper\n3)Scissor\n")
                    i2=input("Enter your choice:")
                print("\nPlayer2 Turn:\n1)Rock\n2)Paper\n3)Scissor\n")
                i3=input("Enter your choice:")
                while i3!="1" and i3!="2" and i3!="3":
                    print("\nPlease enter Valid number!\n")
                    print("\nPlayer2 Turn:\n1)Rock\n2)Paper\n3)Scissor\n")
                    i3=input("Enter your choice:")
                print(f"\nPlayer1 choose {translate_by_num(i2)} and Player2 Choose {translate_by_num(i3)}")
                print(f"Player1 {is_winner(i2,i3)} and Player2 {is_loser(i2,i3)}\n")
                if is_winner(i2,i3)=="Win":
                    no_wins+=1
                    no_loses_p2+=1
                elif is_winner(i2,i3)=="Lose":
                    no_loses+=1
                    no_wins_p2+=1
                elif is_winner(i2,i3)=="Draw":
                    no_draws+=1
                    no_draws_p2+=1
                else:
                    print("Error in Score!")
                i4=input("Do you want to play again?\n1)Yes\n2)No\n")
                while i4!="1" and i4!="2":
                    print("\nPlease enter Valid number!\n")
                    i4=input("Do you want to play again?\n1)Yes\n2)No\n")
                if i4=="1":
                    print("Let's Play again\n")
                elif i4=="2":
                    print(f"\nPlayer1 score:\n{no_wins} Wins  {no_draws} Draws  {no_loses} Loses\n")
                    print(f"Player2 score:\n{no_wins_p2} Wins  {no_draws_p2} Draws  {no_loses_p2} Loses\n")
                    print("Back to ",end="")
                    break
                else:
                    print("I will never show LoL")
        elif i1=="3":
            print("\nBye!\n")
            break
        else:
            print("Please Enter number from 1 to 3!")
except ValueError:
    print("Please Enter Valid Number\n")
except ZeroDivisionError:
    print("Can't Divide by zero!\n")
except TypeError:
    print("Wrong Type Input!")
except OverflowError:
    print("The Numbers are too Long!\n")
except Exception as e:
    print("Unexpected Error:",e,"\n")