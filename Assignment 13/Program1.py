
#------------------------------------------------------------------#
#
#  File Name   : Program1.py
#  Description : Accept N number from user and store it into list
#  Author      : Mayuri Bondge
#  Date        : 14/03/2026
#
#------------------------------------------------------------------#

#------------------------------------------------------------------#
#  Function Name : DisplayAddition()
#  Input         : Accept N number
#  Output        : Return the addition of all element from list
#------------------------------------------------------------------#
def DisplayAddition(No):
    List=[]
    for i in range(1,No+1):
        value=int(input("Enter a number to append the list for addition:"))
        List.append(value)

    Addition=0
    for i in List:
        Addition=Addition+i

    print("Addition of all elemnt is:",Addition)
        
def main():
    Value=0
    Value=int(input("Enter a number:"))
    DisplayAddition(Value)  
        
#------------------------------------------------------------------#
##
##  Starting the execution of the program
##
#------------------------------------------------------------------#
if __name__=="__main__":
    main()

