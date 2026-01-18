################################################################
##
##  File Name   : Program2.py
##  Description : Prints the greater number
##  Author      : Mayuri Bondge
##  Date        : 17/01/2026
##
################################################################


################################################################
##
##  Function Name : CheckGreater
##  Input :         Accept number 
##  Output :        Graeter number
## 
################################################################

def CheckGreater(No1,No2):
    if(No1 > No2):
        print("No1 is greater")
    else:
        print("No2 is greater ")
   
def main():
    CheckGreater(11,20)

    
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()