################################################################
##
##  File Name   : Program4.py
##  Description : Display the cube of number
##  Author      : Mayuri Bondge
##  Date        : 17/01/2026
##
################################################################

################################################################
##
##  Function Name : CubeX
##  Input :         Number 
##  Output :        Cube of given number
## 
################################################################

def CubeX(No):
    print("Square of",No*No*No)

def main():
    print("Enter a number")
    Value=int(input())
    CubeX(Value)

    
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()