# 4chanLurker
##Synopsis
4chaLurker is nothing more than a simple script made for fun, it's only purpose is to fetch and show a random image from one of the specified boards
##Installation
Just download the 4chanLurker folder and make the **4chanlurker.py** file executable:

`chmod +x 4chanlurker.py`

then execute the file with

`./4chanlurker.py`

##Configuration
The **conf.json** file contains the configuration of the script.

-`boards`: this key should be associated with a string which contains one or more board names separated by a single space. This key defines from which boards you'll be pulling the images

-`chanDomain`: this key should be associated with a string which contains the domain of imageboard that hosts the images (The site must implement 4chan's json api, otherwise this script won't work as it is)

-`command`:this key should be associated with a string which contains the command that will be executed when the image is downloaded (the image is passed through STDIN, command chains are not supported)

-`delay`: this key should contain an integer which represents for how long the image will be shown before being closed (number in seconds)

##Enjoy
