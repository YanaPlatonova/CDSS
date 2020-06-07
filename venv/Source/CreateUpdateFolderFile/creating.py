import shutil
import os

def createFolger(newPathFiles):
    if (os.path.exists(newPathFiles) == False):
        os.mkdir(newPathFiles)

def createFiLe(pathFile,newPathFiles):
    if (os.path.exists(newPathFiles + '/' + newPathFiles.split('/')[-1]) == False):
        cmd='copy %s %s' %(pathFile,newPathFiles + '/' + newPathFiles.split('/')[-1]+'.htm')
        # os.popen(cmd)
        shutil.copy2(pathFile, newPathFiles + '/' + newPathFiles.split('/')[-1]+'.htm')