# Print all even elements.

def EvenElemnt(List,size):

     for i in range(size):
         if List[i] % 2==0:
             print(List[i])

def main():
    List=[]
    value=0

    size=int(input("Enter the number of elemnt which can store in list:"))
    
    for i in range(size):
        value=int(input("Enter elemnt: "))
        List.append(value)

    print("Even element is:")
    EvenElemnt(List,size)

if __name__=="__main__":
    main()