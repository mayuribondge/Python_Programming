
def CheckPerfect(No):
    Sum=0

    for i in range(1,(No // 2)+1):
        if No % i ==0:
            Sum=Sum+i

    return Sum==No        

def main():
    Ret=False

    No=int(input("Enter a number:"))
    Ret=CheckPerfect(No)  

    if(Ret==True):
        print("Number is perfect:")
    else:
        print("Number is not perfect:")
        
if __name__=="__main__":
    main()