################################################################
##
##  File Name   : Program2.py
##  Description : Count how many words are present in file
##  Author      : Mayuri Bondge
##  Date        : 05/02/2026
##
################################################################

################################################################
##
##  Function Name : LineCount()
##  Input :         Accept file from user
##  Output :        Count the number of lines in file
##
################################################################


def LineCount(filename):
    linecount = 0
    
    fd = open(filename, 'r')
    
    for line in fd:
        linecount = linecount + 1
    
    return linecount
    fd.close()   

def main():
    FileName = input("Enter a file name: ")
    
    Ret = LineCount(FileName)
    print("Number of lines in file:", Ret)

################################################################
## Starting execution
################################################################

if __name__ == "__main__":
    main()
