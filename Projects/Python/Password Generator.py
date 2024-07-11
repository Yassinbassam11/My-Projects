import random 
upper_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
symbols="@#%&*()_-+;:',./?"
password=""
list=upper_letters+lower_letters+numbers+symbols

print("\nWelcom to Yassin Bassam Password Generator\n")
while True:
    try:
        print("Menu:\n1) Generate Password\n2) Exit")
        i1=input("\nEnter 1 or 2:")
        if i1=="1":
            length=int(input("Enter the Length of the Password:\n"))
            for i in range(length):
                password+=random.choice(list)
            print("\nPassword:",password,"\n")
        elif i1=="2":
            print("\nBye!\n")
            break
        else:
            print("\nPlease enter valid number!\n")
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