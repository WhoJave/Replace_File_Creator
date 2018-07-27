#coding:utf-8

import re
import os

def listFiles(dirPath):

    fileList=[]

    for root,dirs,files in os.walk(dirPath):

        for fileObj in files:

            fileList.append(os.path.join(root,fileObj))

    return fileList



def main():

    fileDir = "/Users/userName/Desktop/dele/dele"#pls change to your project dir

    fileList = listFiles(fileDir)

    for fileObj in fileList:
        if fileObj.endswith(".m") or fileObj.endswith(".h"):
            print fileObj
        f = open(fileObj,'r+')
        all_the_lines=f.readlines()
        pattern = re.compile(ur'by [a-z]+ on')
        for line in all_the_lines:
            if fileObj.endswith(".m") or fileObj.endswith(".h"):
                out = re.sub(pattern,'by BoZhong on',line)
                f.writelines(out)
                print('-----')
                print(out)
                print('***')
        f.close()

if __name__=='__main__':
    main()
