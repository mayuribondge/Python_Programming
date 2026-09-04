def DisplayFactors(No):
    for iCnt in range(1, (No // 2) + 1):
        if No % iCnt == 0:
            print(iCnt)

def main():
    No = int(input("Enter a number:"))
    DisplayFactors(No)


if __name__ == "__main__":
    main()