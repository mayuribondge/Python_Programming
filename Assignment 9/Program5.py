
################################################################
##
##  File Name   : Program5.py
##  Description : Accept name from user and return length of screen
##  Author      : Mayuri Bondge
##  Date        : 26/01/2026
##
################################################################

################################################################
##
##  Function Name : DisplayLength()
##  Input :         String
##  Output :        Display length of string
##
################################################################

def DisplayLength(Data):
    print(len(Data))
        
def main():
    String=input("Enter a string")
    DisplayLength(String)
    

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()