
################################################################
##
##  File Name   : Program2.py
##  Description : Check whether character is vowel or not
##  Author      : Mayuri Bondge
##  Date        : 20/01/2026
##
################################################################

################################################################
##
##  Function Name : CheckCharacter
##  Input :         Character
##  Output :        Vowel or not
## 
################################################################

def CheckCharacter(Ch):

    if Ch=='a' or Ch=='e' or Ch=='i' or Ch=='o' or Ch=='u':
        return True
    
    else:
        return False
            
def main():
    Ret=False
    Character=input("Enter a character to check whether character is vowel or not")
    Ret=CheckCharacter(Character)

    if(Ret==True):
        print("Character is vowel")

    else:
        print("Character is not vowel")

################################################################
##
##  Starting the execution of the program
##
################################################################

if __name__=="__main__":
    main()