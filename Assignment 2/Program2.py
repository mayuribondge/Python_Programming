################################################################
##
##  File Name   : Program2.py
##  Description : Print a sum of first N natural numbers
##  Author      : Mayuri Bondge
##  Date        : 17/01/2026
##
################################################################

################################################################
##
##  Function Name : NaturalNumber
##  Input :         Number 
##  Output :        NaturalNumber
##
################################################################

def NaturalNumbers(No):
    for i in range(1,No+1):
        print(i)
     
def main():
    print("Enter a number to print a multiplication table")
    Value=int(input())
    NaturalNumbers(Value)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()
   