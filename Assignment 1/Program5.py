
################################################################
##
##  File Name   : Program5.py
##  Description : To check whether number is divisible by 3 and 5
##  Author      : Mayuri Bondge
##  Date        : 17/01/2026
##
################################################################

################################################################
##
##  Function Name : CheckDivisible
##  Input :         Number
##  Output :        Number is divisible by 3 and 5s
## 
################################################################

def CheckDivisible(No):

    if(No/3 and No/5):
        print("Number is divisible by 3 and 5:")

    else:
        print("Number is not divisible by 3 and 5:")

def main():
    print("Eneter a number to check whether number is divisible 3 and 5")
    value=int(input())
    CheckDivisible(value)

    
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()