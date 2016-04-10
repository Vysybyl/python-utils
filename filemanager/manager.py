from os import listdir
from os.path import isfile, join, exists, mkdir, remove
from shutil import rmtree


def sync(frompath, topath):
    cnt = 0
    __log("Synchronizing \n" + frompath + "\nto\n" + topath )
    __recursive_sync(frompath, topath, cnt)
    __log("Synchronization completed. " + str(cnt) + " files or directories updated.")

def __recursive_sync(frompath, topath, cnt):
    for f in listdir(frompath):
        if isfile(join(frompath,f)):
            sourcefile = open(join(frompath,f),"r");
            destinationfile = open(join(topath,f),"rw+");
            if sourcefile.read() != destinationfile.read():
                __log("Updating " + join(topath,f))
                cnt += 1
                destinationfile.write(sourcefile.read())
            sourcefile.close()
            destinationfile.close()
        elif isdir(join(frompath,f)):
            if not exists(join(topath,f)):
                mkdir(join(topath,f))
                __log("Creating directory " + join(topath,f))
                cnt += 1
            __recursive_sync(join(frompath,f),join(topath,f), cnt)
    for f in listdir(topath):
        if f not in listdir(frompath):
            if isfile(join(topath,f)):
                __log("Removing file " + join(topath,f))
                remove(join(topath,f))
            elif isdir(join(topath,f)):
                __log("Deleting directory " + join(topath,f))
                rmtree(join(topath,f))

def __log(line):
    echo(line)
