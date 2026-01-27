
################################################################
##
##  File Name   : Program4.py
##  Description : Display first 10 even numbers
##  Author      : Mayuri Bondge
##  Date        : 26/01/2026
##
################################################################

################################################################
##
##  Function Name : DisplayEven()
##  Input :         Number
##  Output :        Display even numbers
##
################################################################

def DisplayEven():
    for i in range(2,22,2):
        print(i)
        
def main():
    DisplayEven()
    

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()