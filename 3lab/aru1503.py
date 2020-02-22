import os 
import fnmatch
import time
from pathlib import Path

def Options():
    print ('''Press 0 to exit
    Press 1 to work with directories 
    Press 2 to change current directory
    Press 3 to work wih files''')

def Dir():
    print('''Press 0 to exit 
        Press 1 to see the number of directories in curret directory
        Press 2 to rename the directory
        Press 3 to see the content of the directory
        Press 4 to add the new directory to current directory
        Press 5 to see the number of files in the directory 
        Press 6 to add the file to the directory''')

def Files():
    print('''Press 0 to exit
        Press 1 to delete the file
        Press 2 to rename the file
        Pres 3 to add content to file 
        Press 4 to rewrite the content 
        Press 5 to retern to the parent directory''' )

def dir_rename(frst,scnd):
    os.rename(frst,scnd)
    print("The name of the directory has changed")

def file_numb():
    entries=os.listdir(currentDir)
    number=int(0)
    for entry in entries:
        if os.path.isfile(entry):
            number+=1
    print("The number of files in this directory is",number,)

def dir_numb():
    entries=os.listdir(currentDir)
    number=int(0)
    for entry in entries:
        if os.path.isdir(entry):
            number+=1
    print("The number of directories in this directory is",number,)

def content_listing_ofDir():
    entries= os.listdir(currentDir)
    for entry in entries:
        print(entry)

def add_file(NameofFile):
    print("Write the name of the new file:")
    currentFile=open(NameofFile,'w')
    print("The new file is added to directory")
    currentFile.close()

def add_dir(NameofDir):
    os.mkdir(NameofDir)

def delete_file(NameofFile):
    os.remove(currentDir +"/"+ NameofFile)
    print("File has been deleted")

def file_rename(frst,scnd):
    os.rename(frst,scnd)
    print("File has been successfully renamed")
def add_file_content(NameofFile):
    currentFile = open(NameofFile, 'a')
    newCont = input("Write the new text: ")
    currentFile.write(newCont)
    print("Content has been successfully added")
    currentFile.close() 

def rewrite_cont(NameofFile):
    currentFile = open(NameofFile, 'w')
    newCont = input("Input the new text: ")
    currentFile.write(newCont)
    print("Contet has been successfully changed")
    currentFile.close()

while True:
    currentDir=os.getcwd()
    Options()
    print("Current directory is:"+currentDir)
    frstButton = int(input("Input: "))
    if frstButton == 1:
        Dir()
        scndButton = int(input("Input: "))
        if scndButton == 1:
            dir_numb()
        elif scndButton == 2:
            frst = input("Enter current directory's name: ")
            scnd = input("Enter directory's new name: ")
            dir_rename(frst,scnd)
            
        elif scndButton == 3:
            content_listing_ofDir()
           
        elif scndButton == 4:
            NameofDir = input("Enterthe new name of directory: ")
            add_dir(NameofDir)
            
        elif scndButton == 5:
            file_numb()
            
        elif scndButton == 6:
            NameofFile = input("Input name of file: ")
            add_file(NameofFile)
            

    elif frstButton == 3:
        Files()
        scndButton = int(input("Input: "))
        if scndButton == 1:
            NameofFile = input("Enter file's name: ")
            delete_file(NameofFile)  
                 
        elif scndButton == 2:
            frst = input("Enter current file's name: ")
            scnd = input("Enter file's new name: ")
            file_rename(frst,scnd)

            
           
        elif scndButton == 3:
            NameofFile = input("Input file's name: ")
            add_file_content(NameofFile)
            
           
        elif scndButton == 4:
            NameofFile = input("Input file's name: ")
            rewrite_cont(NameofFile)

        elif scndButton == 5:
            parentDir = os.path.dirname(os.getcwd())
            os.chdir(parentDir)
            
    elif frstButton == 2:
        newPath = input("Input path: ")
        os.chdir(newPath)
    else:
        print("Thanks, bye")
        time.sleep(1)
        break

