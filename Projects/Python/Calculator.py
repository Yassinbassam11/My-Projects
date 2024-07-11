from math import *

def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def multiply(x,y):
    return(x*y)

def division(x,y):
    try:
        return(x/y)
    except ZeroDivisionError:
        print("Can't divide by Zero")

def power(x,y):
    return(x**y)

def square_root(x):
    return(sqrt(x))

def quadratic_equation(a,b,c):
    if (b**2 - 4*a*c) >=0:
       r1=(-b+(sqrt(b**2 - 4*a*c)))/(2*a)
       r2=(-b-(sqrt(b**2 - 4*a*c)))/(2*a)
       return(r1,r2)
    else:
        u_r=(b**2 - 4*a*c)
        i_num=u_r /(2*a)
        r_num= (-b)/(2*a)
        print(f"R1={r_num}+{i_num} i")
        print(f"R2={r_num}-{i_num} i")

print(quadratic_equation(6,-2,3))
