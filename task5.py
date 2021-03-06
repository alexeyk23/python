# coding=utf-8
import os
import shutil
# 2. запросить входную и выходную дирректорию и скопировать из входной в выходную
# все файлы с расширением .txt в подпапку txt
# все файлы с расширением .rar в подпапку rar и тд


def inputDirName(message):
    nameDir = raw_input(message)
    while(not os.path.isdir(nameDir)):
        nameDir = raw_input(message)
    return nameDir


inpDir = "D:/task4Input/"
outputDir = "D:/task4/"
# inpDir = inputDirName("Enter input directory")+"/"
# outputDir = raw_input("Enter output directory")+"/"
# getList of all files in directory
def getListFiles(inputDir):

    li = []
    for x in os.listdir(inputDir):
        if(os.path.isfile(inputDir+x)):
            li.append(inputDir+x)
        else:
            if(os.path.isdir(inputDir+x)):
                li.extend(getListFiles(inputDir+x+"/"))
    return li
listFiles = getListFiles(inpDir)

copyDir = ""
for x in listFiles:
    t = os.path.splitext(x)[1]
    if(t != ""):
        copyDir = outputDir+t[1:]
        if (not os.path.exists(copyDir)):
            os.makedirs(copyDir)
        shutil.copy(x, copyDir)
print listFiles