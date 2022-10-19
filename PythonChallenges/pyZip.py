"""
zip2folder.py by Dirk Krause, d_krause@pixelpark.com, 12/27/2001

Abstract: A poor man's WinZip

This program does the three essential tasks that (at least) I need:
1. Unzip an archive to a folder
2. Zip a folder to an archive
3. Zip a (big) file to an archive

For convenient usage, get Gordon McMillan's Installer Package, and freeze this application with
> python freeze.py zip2folder.py
After that, you will have a self containing EXE that works even without having python installed.
Drop this thing into the 'sendto' folder, and you have a very convenient way to use this program
via right mouseclick/sendto zip2folder.
"""

import tarfile
import zipfile
import sys
import os
import string


argument = ''
if len(sys.argv) > 1:
    argument = sys.argv[1]
else:
    print('No argument!')

# argument = r'C:\Users\cxa70\Downloads\Django-1.6.2.tar.gz'


MODE_IS_UNKNOWN = 0
MODE_IS_FILE = 1
MODE_IS_ZIPFILE = 2
MODE_IS_DIRECTORY = 3
MODE_IS_TAR = 4

class RecursiveFileIterator:
    # Great script from Daniel Dittmar,
    # http://www.faqts.com/knowledge-base/view.phtml/aid/6000
    def __init__(self, *rootDirs):
        self.dirQueue = list(rootDirs)
        self.includeDirs = None
        self.fileQueue = []

    def __getitem__(self, index):
        while len(self.fileQueue) == 0:
            self.nextDir()
        result = self.fileQueue[0]
        del self.fileQueue[0]
        return result

    def nextDir(self):
        dir = self.dirQueue[0]   # fails with IndexError, which is fine
        # for iterator interface
        del self.dirQueue[0]
        list = os.listdir(dir)
        join = os.path.join
        isdir = os.path.isdir
        for basename in list:
            fullPath = join(dir, basename)
            if isdir(fullPath):
                self.dirQueue.append(fullPath)
                if self.includeDirs:
                    self.fileQueue.append(fullPath)
            else:
                self.fileQueue.append(fullPath)


doit = 0
do_mode = MODE_IS_UNKNOWN

if os.path.isfile(argument):
    if os.path.splitext(argument)[1].lower() == '.zip':
        do_mode = MODE_IS_ZIPFILE
    elif os.path.splitext(argument)[1].lower() == '.tar':
        do_mode = MODE_IS_TAR
    elif os.path.splitext(argument)[1].lower() == '.gz':
        do_mode = MODE_IS_TAR
    else:
        do_mode = MODE_IS_FILE
else:
    do_mode = MODE_IS_UNKNOWN

if os.path.isdir(argument):
    do_mode = MODE_IS_DIRECTORY

if do_mode == MODE_IS_FILE:
    print('converting file %s to zip?' % argument)

if do_mode == MODE_IS_ZIPFILE:
    print('converting zipfile %s to folder?' % argument)

if do_mode == MODE_IS_DIRECTORY:
    print('converting directory %s to zipfile?' % argument)

if do_mode == MODE_IS_TAR:
    print('converting tarfile %s to folder?' % argument)

if do_mode in (MODE_IS_FILE, MODE_IS_ZIPFILE, MODE_IS_DIRECTORY, MODE_IS_TAR):
    # comment the following line to not have to confirm
    if input('[y/n]')[0] in 'yY':
        doit = -1

if do_mode == MODE_IS_UNKNOWN:
    print('%s is not a file.' % argument)

if doit == -1:
    print('ok, doing it.')
else:
    print('exiting.')

if doit == -1 and do_mode == MODE_IS_ZIPFILE:
    zipfilename = argument

    zipdir = os.path.splitext(zipfilename)[0] + '/'

    # if you want the folder to be cleared before unzipping,
    # uncomment the following lines:

    #try:
    #    shutil.rmtree(zipdir)
    #    print 'Deleted',zipdir
    #except: pass


    zipdir = os.path.splitext(zipfilename)[0] + '/'

    file = zipfile.ZipFile(zipfilename, "r")
    print
    'Number of files', len(file.infolist())
    for zfile in file.infolist():
        #print '--------------File:',
        #print zfile.filename, zfile.date_time, zfile.file_size, zfile.compress_size
        dirname = zipdir + os.path.dirname(zfile.filename)

        try:
            os.makedirs(dirname)
        except:
            pass

        if zfile.file_size > 0:
            temp = file.read(zfile.filename)
            # print temp
            fname = zipdir + zfile.filename
            print
            fname
            f = open(fname, "wb").write(temp)

if doit == -1 and do_mode == MODE_IS_TAR:
    tarFileName = argument

    tarDir = os.path.splitext(tarFileName)[0] + '/'

    # if you want the folder to be cleared before unzipping,
    # uncomment the following lines:

    #try:
    #    shutil.rmtree(zipdir)
    #    print 'Deleted',zipdir
    #except: pass

    with tarfile.open(tarFileName, "r") as tar:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, tarDir)

if doit == -1 and do_mode == MODE_IS_DIRECTORY:
    directory = argument

    print
    'directory', os.path.abspath(directory)

    file = zipfile.ZipFile(os.path.abspath(directory) + ".zip", "w")

    for name in RecursiveFileIterator(directory):
        print
        'try', name
        if os.path.isfile(name):
            file.write(name, name, zipfile.ZIP_DEFLATED)

    file.close()

if doit == -1 and do_mode == MODE_IS_FILE:
    file = zipfile.ZipFile(os.path.abspath(argument) + ".zip", "w")
    file.write(argument, argument, zipfile.ZIP_DEFLATED)
    file.close()

# comment the following line to have the dos box disappear immediately
inp = input('<... press the anykey key.>')