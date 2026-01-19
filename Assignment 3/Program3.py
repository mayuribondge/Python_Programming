
################################################################
##
##  File Name   : Program3.py
##  Description : Print Sum of digit of number
##  Author      : Mayuri Bondge
##  Date        : 18/01/2026
##
################################################################

################################################################
##
##  Function Name : SumOfDigit
##  Input :         Number
##  Output :        Sum of digit of number
## 
################################################################

def SumOfDigit(No):
    Sum=0

    while(No!=0):
        Sum=Sum+(No%10)
        No=No//10   
        
    return Sum
        
def main():
    Ret=0
    print("Enter a number to calculate sum of digit")
    Value=int(input())
    Ret= SumOfDigit(Value)
    print("Number of digit in :",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()