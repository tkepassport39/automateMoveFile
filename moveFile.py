import os
import shutil
import getpass
import datetime
import time


while True:
    print("tick")
    # get today's date
    d = datetime.datetime.today()
    # set date format
    d.strftime('%m_%d_%Y')

    # get user currently signed in
    checkUser = getpass.getuser()

    # src directory
    downloadsPath = "/Users/" + checkUser + "/Downloads/"

    # GIMP directory
    gimpDir = "/Users/" + checkUser + "/Pictures/GIMP/downloads/"

    # pictures directory
    picDir = "/Users/" + checkUser + "/Pictures/"

    # list of extension to look for
    ext = [
        ".jpg",
        ".png",
        ".jpeg"
    ]

    # get list of files from src folder
    filesSrc = os.listdir(downloadsPath)
    # get list of files from dst gimp folder
    filesDst = os.listdir(gimpDir)
    # sort all files in src folder
    filesSrc.sort()
    # get the count of files inside dst gimp folder exclude hidden files
    dstGimpFileCount = len([f for f in os.listdir(gimpDir) if not f.startswith('.')])

    # search for files in downloads with following extensions
    for f in filesSrc:
        if f.endswith(tuple(ext)):
            filename = os.path.splitext(f)[0]
            src = downloadsPath + f

            # extract if it starts with "gimp." and drop in gimp folder
            if filename.startswith('gimp.'):
                # increase file num count
                dstGimpFileCount += 1
                # remove "gimp." from file name
                gimpString = filename.replace("gimp.", "")
                # grab file extension
                extension = os.path.splitext(f)[1]
                # rename file
                dst = gimpDir + str(dstGimpFileCount) + "_" + gimpString + "_" + d.strftime('%m_%d_%Y') + extension
                # move file to dst folder
                shutil.move(src, dst)

            # drop pictures in just the normal pictures folder
            else:
                # grab extension of file
                extension = os.path.splitext(f)[1]
                # rename file
                dst = picDir + filename + "_" + d.strftime('%m_%d_%Y') + extension
                # move file to dst folder
                shutil.move(src, dst)

    # hold off X seconds
    time.sleep(5)