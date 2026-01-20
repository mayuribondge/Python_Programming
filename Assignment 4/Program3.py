
################################################################
##
##  File Name   : Program3.py
##  Description : Print Addition multiplication subtraction and division
##  Author      : Mayuri Bondge
##  Date        : 20/01/2026
##
################################################################

################################################################
##
##  Function Name : Operations
##  Input :         Number
##  Output :        Factor of given number
## 
################################################################

def Operations(No1,No2):
    Add=No1+No2
    Sub=No1-No2
    Mul=No1*No2
    Div=No1/No2
    
    return Add,Sub,Mul,Div

def main():
    Ret=0

    print("Enter a first number:")
    Value1=int(input())

    print("Enter a second number:")
    Value2=int(input())

    Ret=Operations(Value1,Value2)

    print("Addition Subtraction multiplication and division Respectively:",Ret)
    

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()