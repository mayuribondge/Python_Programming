
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
Minimum=lambda No: True if No%2==0 else False
    
def main():
    Ret=0
    Value=int(input("Enter a Number:"))
    Ret=Minimum(Value)

    if(Ret==True):
        print("Number is even")

    else:
        print("Number is odd")
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()