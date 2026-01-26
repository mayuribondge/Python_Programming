
################################################################
##
##  File Name   : Program2.py
##  Description : Accept one numberif and check number is even or odd    
##  Author      : Mayuri Bondge
##  Date        : 26/01/2026
##
################################################################

################################################################
##
##  Function Name : Anonymous(Lambda)
##  Input :         Nothing
##  Output :        Display Hello from marvellous
##
################################################################
def CheckNum(No):
    if No %2==0:
        return True
    else:
        return False
    

def main():
    Ret=0
    print("Enter a number")
    Value=int(input())
    Ret=CheckNum(Value)

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

