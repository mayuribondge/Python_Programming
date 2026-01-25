

################################################################
##
##  File Name   : Program2.py
##  Description : Accept number and return true if number is devisible byt 5
##                otherwise false
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
Divisible=lambda No: True if No%5==0 else False
    
def main():
    Ret=0
    Value=int(input("Enter a Number to check number is divisble by 5 or not:"))
    Ret=Divisible(Value)

    if(Ret==True):
        print("Number is divisible by 5")

    else:
        print("Number is not divisible by 5")

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

