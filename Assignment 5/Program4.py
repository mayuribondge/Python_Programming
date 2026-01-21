
################################################################
##
##  File Name   : Program4.py
##  Description : Print binary equivalent
##  Author      : Mayuri Bondge
##  Date        : 21/01/2026
##
################################################################

################################################################
##
##  Function Name : CalculateAreaOfCircle
##  Input :         Number
##  Output :        Display the binary equivalent
##
################################################################

def Equivalent(No):

    Binary=0
    Place=1

    while No > 0:
        Rem = No % 2
        Binary = Binary + (Rem * Place)
        Place = Place * 10
        No = No // 2

    return Binary
    
def main():
    Ret=0
    Value=int(input("Enter anumber"))
    Ret=Equivalent(Value)
    print("Equilvalent is:",Ret)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()