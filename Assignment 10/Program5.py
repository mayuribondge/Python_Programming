
################################################################
##
##  File Name   : Program5.py
##  Description : Check Whether number is prime or not 
##  Author      : Mayuri Bondge
##  Date        : 27/01/2026
##
################################################################

################################################################
##
##  Function Name : CheckPrime()
##  Input :         Accept One number
##  Output :        Display the number is prime or not
##
################################################################
def CheckPrime(No):

    if No <=1:
        return False
    
    for i in range(2,No,1):
        if No % i==0:
            return True

    
def main():
    Ret=0
    Value=int(input("Enter a number to display the Factorial:"))
    Ret=CheckPrime(Value)
    if(Ret==True):
        print("Number is prime")
    else:
        print("Number is not prime")    
   
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

