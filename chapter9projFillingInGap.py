import os, shutil

prefix = 0
for folderName, subFolders, fileNames in os.walk('D:\\pythonSTUFF\\SelectCopyFolder\\'):
    print('The current folder is '+ folderName)
    prefix = int(fileNames[0][:2])-1
    for subfolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in fileNames:
        prefix = prefix+1
        if int(filename[:2]) != prefix:
            newName = str(prefix) + filename[2:]
            shutil.move(folderName+filename, folderName+newName)
        print('FILE INSIDE ' + folderName + ': ' + filename)


    print('')
