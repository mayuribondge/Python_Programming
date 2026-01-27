
################################################################
##
##  File Name   : Program1.py
##  Description : Check whether number if number is positive ,negative or zero
##  Author      : Mayuri Bondge
##  Date        : 26/01/2026
##
################################################################

################################################################
##
##  Function Name : CheckNumber()
##  Input :         Number
##  Output :        Display number if positive,negative or zero
##
################################################################

def CheckNumber(Number):
    if Number < 0:
        print("Number is negative")
    elif Number > 0:
        print("Number is positive")
    else:
        print("Number is zero")

def main():
    Value=int(input("Enter a number:"))
    Ret=CheckNumber(Value)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()

