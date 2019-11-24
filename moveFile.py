import os
import shutil
import getpass
import datetime
import time


while True:
    #print("tick")
    # get today's date
    d = datetime.datetime.today()
    # set date format
    d.strftime('%m_%d_%Y')

    # get user currently signed in
    checkUser = getpass.getuser()

    # setup directory
    downloadsPath = "/Users/" + checkUser + "/Downloads/"

    # pictures directory
    picturesDir = "/Users/" + checkUser + "/Pictures/GIMP/downloaded/"

    # list of extension to look for
    ext = [
        ".jpg",
        ".png",
        ".jpeg"
    ]

    # get list of files from src folder
    filesSrc = os.listdir(downloadsPath)
    # get list of files from dst folder
    filesDst = os.listdir(picturesDir)

    # sort all files in src folder
    filesSrc.sort()
    # get the count of files inside dst folder exclude hidden files
    dstFileCount = len([f for f in os.listdir(picturesDir) if not f.startswith('.')])

    # search for files in downloads with following extensions
    for f in filesSrc:
        if f.endswith(tuple(ext)):
            # increment file num count
            dstFileCount += 1
            extension = os.path.splitext(f)[1]
            src = downloadsPath+f
            # rename file
            dst = picturesDir + str(dstFileCount) + "_pic_" + d.strftime('%m_%d_%Y') + extension
            shutil.move(src, dst)

    # hold off X seconds
    time.sleep(5)