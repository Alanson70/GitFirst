#!/usr/bin/python
import os

def files_find(path):
    arr=os.listdir(path)
    for f in arr:
        if(path!='.'):
            newPath=path+'\\'+f;
        else:
            newPath=f;
        #print(newPath)
        if os.path.isfile(newPath):        
            print(newPath)
        else:            
            if os.path.isdir(newPath):
                files_find(newPath)

            

print('all files in directories and subdirectories')
files_find('.')



