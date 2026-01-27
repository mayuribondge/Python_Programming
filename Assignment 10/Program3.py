
################################################################
##
##  File Name   : Program3.py
##  Description : Accept one number from user display its factorial    
##  Author      : Mayuri Bondge
##  Date        : 27/01/2026
##
################################################################

################################################################
##
##  Function Name : Factorial()
##  Input :         Accept One number
##  Output :        Display factorial of given number
##
################################################################
def Factorial(No):
    Fact=1
    while No !=0:
        Fact=Fact*No
        No=No-1

    return Fact   

def main():
    Ret=0
    Value=int(input("Enter a number to display the Factorail:"))

    Ret=Factorial(Value)
    print("Factorial of number:",Ret)
   
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

