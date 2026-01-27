
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
##  Output :        1 2 3 4 5
##                  1 2 3 4 5
##                  1 2 3 4 5 
##                  1 2 3 4 5
##                  1 2 3 4 5
##
################################################################
def Display(No):

    for i in range(1,No,1):
        for j in range(1,No,1):
            print(j, end=" ")
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

