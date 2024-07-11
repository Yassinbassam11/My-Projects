def simple_calcualtor():
    print("\nWelcome to Yassin Bassam Simple Calculator\n")
    while True:
        try:
            n1=float(input("Enter First number:"))
            op=input("Enter operation:\n1)Sum (+)\n2)Difference (-)\n3)Multiply (*)\n4)Divide (/)\n")
            n2=float(input("Enter Second number:"))
            if op=="+" or op=="1":
                print("Answer= ",(n1+n2),"\n")
            elif op=="-" or op=="2":
                print("Answer= ",(n1-n2),"\n")
            elif op=="*" or op=="3":
                print("Answer= ",(n1*n2),"\n")
            elif op=="/" or op=="4":
                print("Answer= ",(n1/n2),"\n")
            else:
                print("Please Enter Operation from (+,-,*,/)\n")
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
        
simple_calcualtor()
