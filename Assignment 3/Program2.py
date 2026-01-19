
################################################################
##
##  File Name   : Program2.py
##  Description : Print count of digit in that number
##  Author      : Mayuri Bondge
##  Date        : 18/01/2026
##
################################################################

################################################################
##
##  Function Name : CountNumber
##  Input :         Number
##  Output :        Count of given number
## 
################################################################

def CountNumber(No):
    Count=0

    while(No!=0):
        Count=Count+1
        No=No // 10

    return Count
            
def main():
    Ret=0
    print("Enter a number to count how many digit in it")
    Value=int(input())
    Ret= CountNumber(Value)

    print("Number of digit in :",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()