
################################################################
##
##  File Name   : Program1.py
##  Description : Accept one number from user and display pattern 
##  Author      : Mayuri Bondge
##  Date        : 27/01/2026
##
################################################################

################################################################
##
##  Function Name : Display()
##  Input :         Accept One number
##  Output :        * * * * *
##                  * * * *
##                  * * *
##                  * * 
##                  *
##
################################################################
def Display(No):

    for i in range(No,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()    

def main():

    Value=int(input("Enter a number to display the pattern:"))
    Display(Value)
        
   
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":

    main()

