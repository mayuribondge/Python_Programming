################################################################
##
##  File Name   : Program5.py
##  Description :Search the word from the file
##  Author      : Mayuri Bondge
##  Date        : 05/02/2026
##
################################################################

################################################################
##
##  Function Name : SearchWord()
##  Input         : Accept file name from user
##  Output        :  Search the word from file
##
################################################################

def SearchWord(FileName,Word):

    fd=open(FileName,'r')

    Data=fd.read()
        
    if Word in Data:
        print("Word in not present in file")

    else:
        print("This word in not present in file")
    
    fd.close()

def main():
    File=input("Enter a file name:")
    word=input("Enter the word you want to search")

    SearchWord(File,word)
   
################################################################
## Starting execution
################################################################

if __name__ == "__main__":
    main()
