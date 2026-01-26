
################################################################
##
##  File Name   : Program3.py
##  Description : Accept two number and return addition ot given number 
##  Author      : Mayuri Bondge
##  Date        : 26/01/2026
##
################################################################

################################################################
##
##  Function Name : CheckNum()
##  Input :         Accept two number
##  Output :        Display addition of two number
##
################################################################
def CheckNum(No1,No2):
    return No1 + No2
    
def main():
    Ret=0
    print("Enter first number")
    Value1=int(input())

    print("Enter second number")
    Value2=int(input())

    Ret=CheckNum(Value1,Value2)

    print("Additios is:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

