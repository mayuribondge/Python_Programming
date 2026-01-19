
################################################################
##
##  File Name   : Program1.py
##  Description : To check whether number is prime or not
##  Author      : Mayuri Bondge
##  Date        : 18/01/2026
##
################################################################

################################################################
##
##  Function Name : CheckPrime
##  Input :         Number
##  Output :        Prime number
## 
################################################################

def CheckPrime(No):

    if(No % 2==0):
        return True
    else:
        return False

def main():
    Ret=0
    print("Enter a number to check whether number is prime or not")
    value=int(input())
    Ret= CheckPrime(value)

    if(Ret==True):
        print("Number is not prime")

    else:
        print("Number is prime")

    
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()