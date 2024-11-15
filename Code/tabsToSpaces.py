# tabsToSpaces.py
#
# Bryan Daniels
# 07.13.2009
#

import os

def allPythonTabsToSpaces(directory='.',numSpaces=4):
    """
    For all the files ending in '.py' in the given directory, 
    converts tabs to spaces with the specified tab width.
    
    Backs up original copies to filename.py.backup
    """
    originalPath = os.getcwd()
    os.chdir(directory)
    for filename in os.listdir('.'):
        if filename[-3:] == '.py':
            backupFilename = filename + '.backup'
            os.rename(filename,backupFilename)
            tabsToSpaces(backupFilename,filename,numSpaces)
            print str(numSpaces)+"-space tabs -> spaces in "+filename
            print "        Original moved to",backupFilename
    os.chdir(originalPath)

def tabsToSpaces(filename,newFilename,numSpaces=4):

    fin = open(filename,'r')
    fout = open(newFilename,'w')

    newLines = []

    for line in fin.readlines():
        i = 0
        while i+1<len(line):
            for i,l in enumerate(line):
                if l=='\t':
                    insertSpaces = ''
                    for j in range(numSpaces-i%numSpaces):
                        insertSpaces += ' '
                    line = line.replace('\t',insertSpaces,1)
                    break
        newLines.append(line)
        
    fout.writelines(newLines)
