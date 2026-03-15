#------------------------------------------------------------------#
##
##  File Name   : Program3.py
##  Description : Accept N number from user and store it into list
##  Author      : Mayuri Bondge
##  Date        : 14/03/2026
##
#------------------------------------------------------------------#

#------------------------------------------------------------------#
##
##  Function Name : DisplayMinimum()
##  Input         : Accept N number
##  Output        : Return the Minimum number from list from list
##
#------------------------------------------------------------------#
def DisplayMinimum(No):
    List=[]
    for i in range(1,No+1):
        value=int(input("Enter a number to check which number is minimum:"))
        List.append(value)

    Min=List[0]
    for i in List:
        if i < Min:
            Min=i
    return Min
        
def main():
    Value=0
    Ret=0
    Value=int(input("Enter a number:"))
    Ret= DisplayMinimum(Value)  
    print("Minimum number is:",Ret)
        
#------------------------------------------------------------------#
##
##  Starting the execution of the program
##
#------------------------------------------------------------------#
if __name__=="__main__":
    main()
