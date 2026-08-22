# Find the sum of elements at even indexes.

def SumEvenIndex(List,size):
    Sum=0
    for i in range(0,size):
        if i % 2!=0:
            Sum=Sum+List[i]
    return Sum        

def main():
    List=[10,15,20,25,30]
    size=len(List)

    Ret=SumEvenIndex(List,size)

    print("sum of elements at even indexes:",Ret)

if __name__=="__main__":
    main()