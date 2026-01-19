################################################################
##
##  File Name   : Program1.py
##  Description : Print a Multiplication of table
##  Author      : Mayuri Bondge
##  Date        : 17/01/2026
##
################################################################

################################################################
##
##  Function Name : Multiplication
##  Input :         Number 
##  Output :        Multiplication of number
##
#################################################################
def Multiplication(No):
    for i in range(1,11,1):
        print(No*i)
     
 
def main():
    print("Enter a number to print a multiplication table")
    Value=int(input())
    Multiplication(Value)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()