# Automate Move File

This python script is running as a daemon in the background on my iMac. It is automating the process of moving image files (jpg, png, jpeg) from my downloads folder to another destination folder.

I was tired of having to move these files manually. Therefore, this will now save me the headache. 

### Setting up the daemon files
Article on how to setup [launchctl](https://medium.com/@chetcorcos/a-simple-launchd-tutorial-9fecfcf2dbb3) on a Mac. Another article from [Stack overflow](https://stackoverflow.com/questions/29338066/mac-osx-execute-a-python-script-at-startup).

Save the plist file in `~/library/launchagent` folder

## How the code works

Python script is looking for files with extensions (jpg, png, jpeg) in my downloads folder every 5 seconds. If it finds a file with such extension, it will move it to my `pictures` directory and rename the file to include the date. 

If the image has `gimp.` as part of the name. It will move the images to a dedicated gimp folder `pictures/gimp/downloads` and rename the file.

*Example gif below*:

![moveFiles](./images/pythonMoveFiles.gif)