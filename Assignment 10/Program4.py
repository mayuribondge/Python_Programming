
################################################################
##
##  File Name   : Program4.py
##  Description : Accept one number from user display the addition of its factorial    
##  Author      : Mayuri Bondge
##  Date        : 27/01/2026
##
################################################################

################################################################
##
##  Function Name : FactorialSum()
##  Input :         Accept One number
##  Output :        Display the addition of its factorial
##
################################################################
def FactorialSum(No):
    Fact=1
    Sum=0
    while No !=0:
        Fact=Fact+No
        No=No-1

    return Fact    

def main():
    Ret=0
    Value=int(input("Enter a number to display the Factorial:"))

    Ret=FactorialSum(Value)
    print("Factorial of number:",Ret)
   
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

