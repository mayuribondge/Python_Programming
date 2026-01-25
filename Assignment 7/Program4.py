

################################################################
##
##  File Name   : Program3.py
##  Description : Accept two number and return multiplication number       
##  Author      : Mayuri Bondge
##  Date        : 25/01/2026
##
################################################################

################################################################
##
##  Function Name : Anonymous(Lambda)
##  Input :         Accept two number
##  Output :        Display multiplication of number
##
################################################################
Multiplication=lambda No1,No2:No1*No2
    
def main():
    Ret=0
    Value1=int(input("Enter a first number:"))
    Value2=int(input("Enter a second number:"))
    Ret=Multiplication(Value1,Value2)
    print("Multiplication is:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

