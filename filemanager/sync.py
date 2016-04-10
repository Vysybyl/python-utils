from os import listdir, mkdir,remove
from os.path import isfile, join, exists, isdir
from shutil import rmtree
import sys


def sync(frompath, topath):
    __log("Synchronizing \n" + frompath + "\nto\n" + topath )
    cnt = __recursive_sync(frompath, topath)
    __log("Synchronization completed. " + str(cnt) + " files or directories updated.")

def __recursive_sync(frompath, topath):
    cnt = 0
    for f in listdir(frompath):
        if isfile(join(frompath,f)):
            sourcefile = open(join(frompath,f),"r");
            if not isfile(join(topath,f)):
                cnt = cnt + 1
                __log("Creating new file " + join(topath,f))
            destinationfile = open(join(topath,f),"w+");
            if sourcefile.read() != destinationfile.read():
                __log("Updating " + join(topath,f))
                cnt = cnt + 1
                destinationfile.write(sourcefile.read())
            sourcefile.close()
            destinationfile.close()
        elif isdir(join(frompath,f)):
            if not exists(join(topath,f)):
                mkdir(join(topath,f))
                __log("Creating directory " + join(topath,f))
                cnt = cnt + 1
            cnt = cnt + __recursive_sync(join(frompath,f),join(topath,f))
    for f in listdir(topath):
        if f not in listdir(frompath):
            if isfile(join(topath,f)):
                __log("Removing file " + join(topath,f))
                remove(join(topath,f))
            elif isdir(join(topath,f)):
                __log("Deleting directory " + join(topath,f))
                rmtree(join(topath,f),True)
    return cnt

def __log(line):
    print(line)

if __name__ == "__main__":
    args = sys.argvs
    if len(args) <3:
        print("This script requires 2 arguments!")
    else:
        synch(args[1],args[2])
