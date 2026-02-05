################################################################
##
##  File Name   : Program2.py
##  Description : Copy content of one file into another
##  Author      : Mayuri Bondge
##  Date        : 05/02/2026
##
################################################################

################################################################
##
##  Function Name : CopyFile()
##  Input :         Accept Source file and destination file
##  Output :        Copy content one file into another
##
################################################################

def CopyFile(SourceFile, DestinationFile):
    
    src = open(SourceFile, 'r')        
    dest = open(DestinationFile, 'w')  
    
    for line in src:                   
        dest.write(line)              
    
    src.close()
    dest.close()

def main():
    File1 = input("Enter source file name: ")
    File2 = input("Enter destination file name: ")
    
    CopyFile(File1, File2)
    print("File copied successfully")

################################################################
## Starting execution
################################################################

if __name__ == "__main__":
    main()
