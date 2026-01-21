
################################################################
##
##  File Name   : Program3.py
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

def CalculateAreaOfCircle(No):
    Sum=0
    for i in range(1,No):
        if(No % i==0):
            print(i)
            Sum=Sum+i
    return Sum

def main():
    Ret=0
    Value=0
    print("Enter a number of check number is perfect or not")
    Value=int(input())
    Ret=CalculateAreaOfCircle(Value)

    if(Ret==Value):
        print("Number is perfect")

    else:
        print("Number is not perfect")

   
################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()