
################################################################
##
##  File Name   : Program4.py
##  Description : Print Sum a reverse of that number
##  Author      : Mayuri Bondge
##  Date        : 19/01/2026
##
################################################################

################################################################
##
##  Function Name : ReverseDigit
##  Input :         Number
##  Output :        Revese of given number
## 
################################################################


def ReverseDigit(No):
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
    Ret= ReverseDigit(Value)
    print("Revesrse of number :",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()
