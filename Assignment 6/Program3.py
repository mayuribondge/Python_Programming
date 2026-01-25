
################################################################
##
##  File Name   : Program3.py
##  Description : Accept two number and return maximum number
##  Author      : Mayuri Bondge
##  Date        : 25/01/2026
##
################################################################

################################################################
##
##  Function Name : Anonymous(Lambda)
##  Input :         Accept two number
##  Output :        Display maximum number
##
################################################################
Maximum=lambda No1,No2 : No2 if No1<No2 else No1
    
def main():
    Ret=0
    Value1=int(input("Enter a first Number"))
    Value2=int(input("Enter a second number"))
    Ret=Maximum(Value1,Value2)
    print("Maximum number:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()