# Final version
# Sage Katwala 12/12/2023

# get "INTERNAL_NAME" element from xml files

####-----------------------------------------------##
import os
#import pandas


# create list of usable folders

##folderdir1 = os.listdir(r"Z:/cta-archives/")

##folderdir =[]
##for project in folderdir1:
##
##    if project == "01_CTA Archives - Shortcut.lnk":
##        print("skip", project)
##    elif project == "UM_ProjectNet Archive Access Quick Start_20150501.pdf":
##        print("skip", project)
##    elif project == "Thumbs.db":
##        print("skip", project)
##    else:
##        print(project)
##        folderdir.append(project)
##    print(folderdir)

## !!!!### I ran the whole script and it stopped at "Design Services - MEC Contract - Muller and Muller"
## because the folder paths are formatted totally different, so this is the list of the rest:
##folderdir = ["Design Signals Orange Line and Loop Upgrades","Design Substations Farwell Armitage Hill BreakerRoom","Design Traction Power Systemwide Upgrades and Improvements_37", "Douglas Art Program","Garfield Park n Ride", "Harrison Curve Realignment_7","Improve Bus Turnarounds Mad Aus Hal Wav Hal Bel Gnd Nor","Planning CTA Rail Station ADA Assessment_34"]
folderdir = ["Improve BusTurnarounds Mad Aus Hal Wav Hal Bel Gnd Nor","Planning CTA Rail Station ADA Assessment_34"]

####
# change working directory to simplify path names
os.chdir('C:/Users/skatwala.int/OneDrive - Chicago Transit Authority/pnetmapping/testingdocs/new2/')
#print(os.getcwd())

# project name is folder name, 
for project in folderdir:

    csvName = project + ".csv"
    print("csvName:", csvName)
    subpath = r"Z:/cta-archives/" + project + "/Documents/Metadata"
    csvfile = open(csvName, 'a')
    # set headers:
    csvfile.write("XMLfilename, INTERNAL_NAME, \n")

    # get basic directory list of metadata folder contents
    dirlist = os.listdir(subpath)
    # set up empty list
    xmllist = []

     # populate list of xml files
    for item in dirlist:
        if "xml" in item:
            xmllist.append(item)

    for xml in xmllist:
        # create variable for path of xml file to open and read
        xmlfilepath = r"Z:/cta-archives/" + project + r"/Documents/Metadata/" + xml
        file = open(xmlfilepath)
            
        lines = file.readlines()
        
        for line in lines:
            
            if "INTERNAL_NAME" in line:
                
                intname = line.replace("<INTERNAL_NAME>","").replace("</INTERNAL_NAME>","")
                print(intname)
                writeline = xml + "," + intname #+ "\n"
                csvfile.write(writeline)
                

    csvfile.close()
    print("done", xmlfilepath)
    

