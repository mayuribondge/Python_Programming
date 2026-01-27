
################################################################
##
##  File Name   : Program4.py
##  Description : Accept one number from user and return number of digit in that number
##  Author      : Mayuri Bondge
##  Date        : 27/01/2026
##
################################################################

################################################################
##
##  Function Name : DisplayDigit()
##  Input :         Accept One number
##  Output :        Count the number of digit
##
##
################################################################
def DisplayDigit(No):
    Count=0

    while No!=0:
        Count=Count+1
        No=No//10
    return Count
    
def main():
    Ret=0
    Value=int(input("Enter a number to display the pattern:"))
    Ret=DisplayDigit(Value)
    print("Number of digits are:",Ret)
        
   
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

