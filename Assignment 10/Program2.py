
################################################################
##
##  File Name   : Program2.py
##  Description : Accept one number and display below pattern    
##  Author      : Mayuri Bondge
##  Date        : 27/01/2026
##
################################################################

################################################################
##
##  Function Name : Display()
##  Input :         Accept One number
##  Output :        * * * * *
##                  * * * * *
##                  * * * * *
##
################################################################
def Display(No):
    for i in range(1,No,1):
        for j in range(1,No,1):
            print("*\t",end=" ")
        print()

def main():
    Ret=0
    Value=int(input("Enter a number to display the pattern:"))

    Display(Value)
   
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

