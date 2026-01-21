
################################################################
##
##  File Name   : Program5.py
##  Description : Print binary equivalent
##  Author      : Mayuri Bondge
##  Date        : 20/01/2026
##
################################################################

################################################################
##
##  Function Name : CalculateAreaOfCircle
##  Input :         Number
##  Output :        Display the binary equivalent
##
################################################################

def DisplayGrade(Marks):

    if(Marks>=75):
        print("Destination")

    elif(Marks>=60):
        print("First Class")

    elif(Marks>=50):
        print("Second class")

    elif(Marks<=50):
        print("Fail")

    else:
        print("Please enter a marks")
    
    
def main():

    Value=int(input("Enter a marks"))
    DisplayGrade(Value)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()