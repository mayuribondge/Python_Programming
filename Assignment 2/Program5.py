################################################################
##
##  File Name   : Program5.py
##  Description : Print all odd number till that bumber
##  Author      : Mayuri Bondge
##  Date        : 17/01/2026
##
################################################################

################################################################
##
##  Function Name : OddNumbers
##  Input :         Number 
##  Output :        Odd number till you enter
##
################################################################

def OddNumbers(No):
    for i in range(1,No+1,1):
        if(i%2!=0):
            print(i)
     
def main():
    print("Enter a number to print even number till that number")
    Value=int(input())
    OddNumbers(Value)

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()
   