
################################################################
##
##  File Name   : Program5.py
##  Description : Accept one number and print in reverse order
##  Author      : Mayuri Bondge
##  Date        : 20/01/2026
##
################################################################

################################################################
##
##  Function Name : PrintReverse
##  Input :         Number
##  Output :        Display the numbers in reverse order
## 
################################################################

def PrintReverse(No):

    for i in range(No,0,-1):
        print(i)

     

def main():
    Ret=0

    print("Enter a first number:")
    Value=int(input())

    Ret= PrintReverse(Value)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()