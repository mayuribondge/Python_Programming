
################################################################
##
##  File Name   : Program5.py
##  Description : Accept number and return trur if number even otherwise false
##  Author      : Mayuri Bondge
##  Date        : 25/01/2026
##
################################################################

################################################################
##
##  Function Name : Anonymous(Lambda)
##  Input :         Accept one number
##  Output :        Display number is even or odd
##
################################################################
Minimum=lambda No: True if No%2==0 else False
    
def main():
    Ret=0
    Value=int(input("Enter a Number to check number is even or odd:"))
    Ret=Minimum(Value)

    if(Ret==True):
        print("Number is even")

    else:
        print("Number is odd")
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

