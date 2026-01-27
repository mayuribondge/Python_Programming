
################################################################
##
##  File Name   : Program3.py
##  Description : Accept number from user and print that number on "*"
##  Author      : Mayuri Bondge
##  Date        : 26/01/2026
##
################################################################

################################################################
##
##  Function Name : Display()
##  Input :         Number
##  Output :        Display * from console
##
################################################################

def Display(Number):
    for i in range(Number):
        print("*")

def main():
    Value=int(input("Enter a number:"))
    Display(Value)

    

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()