
#------------------------------------------------------------------#
##
##  File Name   : Program2.py
##  Description : Accept N number from user and store it into list
##  Author      : Mayuri Bondge
##  Date        : 14/03/2026
##
#------------------------------------------------------------------#

#------------------------------------------------------------------#
##
##  Function Name : DisplayMaximum()
##  Input         : Accept N number
##  Output        : Return the maximum number from list from list
##
#------------------------------------------------------------------#
def DisplayMaximum(No):
    List=[]
    for i in range(1,No+1):
        value=int(input("Enter a number to append the list for addition:"))
        List.append(value)

    Max=0
    for i in List:
        if i > Max :
            Max=i
    return Max
        
def main():
    Value=0
    Ret=0
    Value=int(input("Enter a number:"))
    Ret= DisplayMaximum(Value)  
    print("Maximum number is:",Ret)
        
#------------------------------------------------------------------#
##
##  Starting the execution of the program
##
#------------------------------------------------------------------#
if __name__=="__main__":
    main()
