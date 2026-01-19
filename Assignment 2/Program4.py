################################################################
##
##  File Name   : Program4.py
##  Description : Print all even number till that bumber
##  Author      : Mayuri Bondge
##  Date        : 17/01/2026
##
################################################################

################################################################
##
##  Function Name : EvenNumbers
##  Input :         Number 
##  Output :        Even number till you enter
##
################################################################

def EvenNumbers(No):
    for i in range(1,No+1,1):
        if(i%2==0):
            print(i)
     
def main():
    print("Enter a number to print even number till that number")
    Value=int(input())
    EvenNumbers(Value)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()
   