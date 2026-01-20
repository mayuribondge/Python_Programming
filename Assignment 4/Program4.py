
################################################################
##
##  File Name   : Program4.py
##  Description : Accept one number and print starting from1
##  Author      : Mayuri Bondge
##  Date        : 20/01/2026
##
################################################################

################################################################
##
##  Function Name : PrintStartingNum
##  Input :         Number
##  Output :        Factor of given number
## 
################################################################

def PrintStartingNum(No):

    for i in range(1,No+1,1):
        print(i)

    
def main():
    Ret=0

    print("Enter a first number:")
    Value=int(input())

    Ret= PrintStartingNum(Value)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()