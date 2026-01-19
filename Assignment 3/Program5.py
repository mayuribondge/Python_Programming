
################################################################
##
##  File Name   : Program5.py
##  Description : Check Whether number is palindrome or not
##  Author      : Mayuri Bondge
##  Date        : 18/01/2026
##
################################################################

################################################################
##
##  Function Name : CheckPrime
##  Input :         Number
##  Output :        Palindrome number
## 
################################################################


def  CheckPrime(No):
    rev=0
    while(No!=0):
        digit=0
    
        digit= No % 10
        rev=rev*10+digit
        No=No//10  

    return rev
        
def main():
    Ret=0
    print("Enter a number to reverse that number")
    Value=int(input())
    Ret=  CheckPrime(Value)

    if(Ret==Value):
        print("Number is palindrome")

    else:
        print("Number is not panlindrome")


################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()