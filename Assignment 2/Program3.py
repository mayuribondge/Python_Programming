################################################################
##
##  File Name   : Program3.py
##  Description : Print a facorial of numbers
##  Author      : Mayuri Bondge
##  Date        : 17/01/2026
##
################################################################

################################################################
##
##  Function Name : Factorial
##  Input :         Number 
##  Output :        Factorial of given number
##
################################################################

def Factorial(No):
    Fact=1
    for i in range(1,No+1,1):
        Fact=Fact*i
    return Fact
        
     
def main():
    Ret=0
    print("Enter a number to print a Factorial of number")
    Value=int(input())
    Ret=Factorial (Value)
    print("Factorial of a given number is:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()
   