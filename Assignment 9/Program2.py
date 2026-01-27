
################################################################
##
##  File Name   : Program2.py
##  Description : Return true if number is divisible by 5 otherwise false
##  Author      : Mayuri Bondge
##  Date        : 26/01/2026
##
################################################################

################################################################
##
##  Function Name : DivisibleBy()
##  Input :         Number
##  Output :        Display number is divided by 5
##
################################################################

def DivisibleBy(Number):

    if Number %5==0:
        return True
    else:
        return False
def main():
    Value=int(input("Enter a number:"))
    Ret=DivisibleBy(Value)

    if Ret==True:
        print("True")
    else:
        print("False")    

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()

