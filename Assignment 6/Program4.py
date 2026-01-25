
################################################################
##
##  File Name   : Program4.py
##  Description : Accept two number and return minimum number
##  Author      : Mayuri Bondge
##  Date        : 25/01/2026
##
################################################################

################################################################
##
##  Function Name : Anonymous(Lambda)
##  Input :         Accept two number
##  Output :        Display minimum number
##
################################################################
Minimum=lambda No1,No2 : No1 if No1<No2 else No2
    
def main():
    Ret=0
    Value1=int(input("Enter a first Number"))
    Value2=int(input("Enter a second number"))
    Ret=Minimum(Value1,Value2)
    print("Minimum number:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()