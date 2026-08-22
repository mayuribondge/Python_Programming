# Find the largest even number

def LargestEvenNumber(List,size):
    num=List[0]
    for i in range(1,size):
        if num < List[i] and num % 2==0:
            num=List[i]

    return num        

def main():
    List=[]

    size=int(input("Enter a number to store number in list:"))

    for i in range(size):
        value=int(input("Enter a number:"))
        List.append(value)

    Ret=LargestEvenNumber(List,size) 
    print(Ret)   

if __name__=="__main__":
    main()