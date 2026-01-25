
################################################################
##
##  File Name   : Program1.py
##  Description : Accept one number and return square that number
##  Author      : Mayuri Bondge
##  Date        : 25/01/2026
##
################################################################

################################################################
##
##  Function Name : Anonymous(Lambda)
##  Input :         Number
##  Output :        Display square of given number
##
################################################################
SquareX= lambda Number:Number*Number

def main():
    Ret=0
    Value=int(input("Enter a Number"))
    Ret=SquareX(Value)
    print("Number of square:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()