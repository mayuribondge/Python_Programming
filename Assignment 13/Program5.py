
#------------------------------------------------------------------#
#
#  File Name   : Program5.py
#  Description : Accept N number from user and store it into list
#                and check wwhether number is prime or not
#                return addition of all prime numbers        
#  Author      : Mayuri Bondge
#  Date        : 15/03/2026
#
#------------------------------------------------------------------#

import CheckPrimeModule

#------------------------------------------------------------------#
#
#  Function Name : ListPrime()
#  Input         : Accept N number 
#  Output        : Return addition of all prime numbers
#
#------------------------------------------------------------------#
def ListPrime(num):

    List=[]
    Sum=0

    for i in range(1,num+1):
        value=int(input("Enter a number"))
        List.append(value)

    for i in List:
        Ret=CheckPrimeModule.CheckPrime(i)

        if(Ret==True):
            Sum=Sum+i

    return Sum

def main():
    Ret=0
    value=int(input("Enter a numer to append the list"))
    Ret= ListPrime(value)
    print("Addion of prime number is:",Ret)
    
#------------------------------------------------------------------#
#  Starting the execution of the program
#------------------------------------------------------------------#
if __name__=="__main__":
    main()
