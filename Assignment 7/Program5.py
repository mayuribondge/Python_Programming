

################################################################
##
##  File Name   : Program5.py
##  Description : Accept three number and return largest number       
##  Author      : Mayuri Bondge
##  Date        : 25/01/2026
##
################################################################

################################################################
##
##  Function Name : Anonymous(Lambda)
##  Input :         Accept three number
##  Output :        Display the largest of number
##
################################################################
Multiplication=lambda No1,No2,No3:No1 if( No1>No2 and No1>No3) else( No2 if No2>No1 and No2>No3 else No3)
    
def main():
    Ret=0
    Value1=int(input("Enter a first number:"))
    Value2=int(input("Enter a second number:"))
    Value3=int(input("Enter a third number:"))
    Ret=Multiplication(Value1,Value2,Value3)
    print("Largest Number is:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

