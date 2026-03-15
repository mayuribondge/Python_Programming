
#------------------------------------------------------------------#
#
#  File Name   : Program4.py
#  Description : Accept N number from user and store it into list
#                accept one from user and return frequency of that give number         
#  Author      : Mayuri Bondge
#  Date        : 15/03/2026
#
#------------------------------------------------------------------#

#------------------------------------------------------------------#
#
#  Function Name : DisplayFrequency()
#  Input         : Accept N number and accept one to check the frequency count
#  Output        : Return frequency of that give number
#
#------------------------------------------------------------------#
def DisplayFrequency(No,freq):
    List=[]
    Count=0
    for i in range(1,No+1):
        value=int(input("Enter a number:"))
        List.append(value)

    for i in List:
        if(i==freq):
            Count=Count+1
    return Count

def main():

    Value1=int(input("Enter a number to how many numbers append to list:"))
    value2=int(input("Enter a number to check frequency count :"))

    Ret= DisplayFrequency(Value1,value2)  
    print(f"Frequency of {value2} is {Ret}")
        
#------------------------------------------------------------------#
#  Starting the execution of the program
#------------------------------------------------------------------#
if __name__=="__main__":
    main()
