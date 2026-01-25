
################################################################
##
##  File Name   : Program2.py
##  Description : Accept one number and return Cube that number
##  Author      : Mayuri Bondge
##  Date        : 25/01/2026
##
################################################################

################################################################
##
##  Function Name : Anonymous(Lambda)
##  Input :         Number
##  Output :        Display Cube of given number
##
################################################################
CubeX= lambda Number:Number*Number*Number

def main():
    Ret=0
    Value=int(input("Enter a Number"))
    Ret=CubeX(Value)
    print("Number of Cube:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()