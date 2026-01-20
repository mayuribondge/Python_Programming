
################################################################
##
##  File Name   : Program2.py
##  Description : Accept one number and prints its factor
##  Author      : Mayuri Bondge
##  Date        : 20/01/2026
##
################################################################

################################################################
##
##  Function Name : PrintFactor
##  Input :         Number
##  Output :        Factor of given number
## 
################################################################

def PrintFactor(No):

    for i in range(1,No+1,1):

        if(No % i==0):
            print(i)

def main():

    Value=int(input("Enter a number to find factor"))
    PrintFactor(Value)
    
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()