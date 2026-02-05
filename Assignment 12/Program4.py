################################################################
##
##  File Name   : Program4.py
##  Description : Read the data from file
##  Author      : Mayuri Bondge
##  Date        : 05/02/2026
##
################################################################

################################################################
##
##  Function Name : ReadData()
##  Input         : Accept file name from user
##  Output        : Display data from file
##
################################################################

def ReadData(FileName):

    fd=open(FileName,'r')

    Data=fd.read()
        
    if Data=='':
        print("File is empty")

    else:
        print(Data)
    
    fd.close()

def main():
    File=input("Enter a file name:")
  
    SearchWord(File)
   
################################################################
## Starting execution
################################################################

if __name__ == "__main__":
    main()
