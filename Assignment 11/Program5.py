
################################################################
##
##  File Name   : Program5.py
##  Description : Accept one number from user and return addition of digit in that number
##  Author      : Mayuri Bondge
##  Date        : 27/01/2026
##
################################################################

################################################################
##
##  Function Name : DisplayDigit()
##  Input :         Accept One number
##  Output :        Return the addition of digit
##
##
################################################################
def DisplayDigit(No):
    Count=0
    Sum=0
    Max=0
    while No!=0:
        Digit=No%10
        Sum=Sum+Digit
        No=No//10
    return Sum
    
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

