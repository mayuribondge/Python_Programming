################################################################
##
##  File Name   : Program3.py
##  Description : Display the number of square
##  Author      : Mayuri Bondge
##  Date        : 17/01/2026
##
################################################################

################################################################
##
##  Function Name : SqareX
##  Input :         Number 
##  Output :        Square of given number
## 
################################################################

def SqareX(No):
    print("Square of",No*No)

def main():
    print("Enter a number")
    Value=int(input())
    SqareX(Value)


################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()