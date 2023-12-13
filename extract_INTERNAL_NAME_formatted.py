# Sage Katwala 12/12/2023

# get "INTERNAL_NAME" element from xml files

####-----------------------------------------------##
import os
import pandas


# create list of usable folders

folderdir1 = os.listdir(r"Z:/cta-archives/")
print(folderdir1)
folderdir =[]
for project in folderdir1:

    if project == "01_CTA Archives - Shortcut.lnk":
        print("skip", project)
    elif project == "UM_ProjectNet Archive Access Quick Start_20150501.pdf":
        print("skip", project)
    elif project == "Thumbs.db":
        print("skip", project)
    else:
        print(project)
        folderdir.append(project)
print(folderdir)

####
# change working directory to simplify path names
os.chdir('C:/Users/skatwala.int/OneDrive - Chicago Transit Authority/pnetmapping/testingdocs/new2/')
#print(os.getcwd())


for project in folderdir:
    csvName = project + ".csv"
    subpath = r"Z:/cta-archives/" + project + "/Documents/Metadata"
    csvfile = open(csvName, 'a')
    csvfile.write("XMLfilename, INTERNAL_NAME, \n")
