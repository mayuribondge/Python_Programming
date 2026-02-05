################################################################
##
##  File Name   : Program3.py
##  Description : Write the data into the file
##  Author      : Mayuri Bondge
##  Date        : 05/02/2026
##
################################################################

################################################################
##
##  Function Name : WriteIntoFile()
##  Input :         Accept Source file and destination file
##  Output :        Copy content one file into another
##
################################################################

def WriteIntoFile(FileName):

    FileName=open(FileName,'w')

    FileName.write("Name: Mayuri Bondge\n")

    if(FileName==None):
        return False
    
    else:
        return True

def main():
    File=input("Enter a file name:")

    Ret=WriteIntoFile(File)

    if Ret==True:
        print("Written data successfully")
    else:
        print("Unable to write the data into the file")    

################################################################
## Starting execution
################################################################

if __name__ == "__main__":
    main()
