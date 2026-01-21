
################################################################
##
##  File Name   : Program5.py
##  Description : Accept width and height Calculate the area
##  Author      : Mayuri Bondge
##  Date        : 20/01/2026
##
################################################################

################################################################
##
##  Function Name : CalculateArea
##  Input :         width and height
##  Output :        Display the area
##
################################################################

def CalculateArea(No1,No2):

    Area=0
    Area=No1 * No2
    return Area   

def main():
    Ret=0

    print("Enter a Width")
    Width=int(input())
    
    print("Enter a Width")
    Height=int(input())

    Ret=CalculateArea(Height,Width)

    print("Area is:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()