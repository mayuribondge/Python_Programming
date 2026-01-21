
################################################################
##
##  File Name   : Program5.py
##  Description : Calculate the area of circle
##  Author      : Mayuri Bondge
##  Date        : 20/01/2026
##
################################################################

################################################################
##
##  Function Name : CalculateAreaOfCircle
##  Input :         Radius
##  Output :        Display the area of circle
##
################################################################

def CalculateAreaOfCircle(Rd):

    Circle=3.14*Rd*Rd
    return Circle

def main():
    Ret=0

    print("Enter a Radius")
    Radius=int(input())
    Ret=CalculateAreaOfCircle(Radius)

    print("Area of circle is:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()