# Find the average of even elements

def AverageEvenIndex(List,size):
    avg=0
    count=0

    for i in range(0,size):
        if List[i] % 2==0:
            avg=avg+List[i]
            count=count+1

    return avg / count;  

def main():
    List=[10,15,20,25,30]
    size=len(List)

    Ret=AverageEvenIndex(List,size)

    print("average of even elements:",Ret)

if __name__=="__main__":
    main()