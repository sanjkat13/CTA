# Sage Katwala 12/13/2023

# write XML into Excel file for PNet mapping

import os

# Metadata folder path:
#Arts in Transit
## project = input("copy and paste folder name: ")
project = "Arts in Transit" # temp for test

mdPath = r"Z:/cta-archives/"+  project + "/Documents/Metadata"
print(mdPath)

csvName = project + ".csv"
# create new csv file
csvfile = open(csvName, 'a')

#headers:
#0 Document File Name
#1 Type
#2 Document Type
#3 Document File Name
#4 Creation Date
#5 Description
#6 [Author]
#7 [Designed By]
#8 [Document Title/Sheet Name]
#9 Document Category
#10 Document Category
#11 Document Type
#12 Project Name

# (make sure there aren't any spaces before each item in the list)
# write headers
csvfile.write("FilePath, Document File Name,Type,Document Type,Document File Name,Creation Date,Description,[Author],[Designed By],[Document Title/Sheet Name],Document Category,Document Category,Document Type,Project Name, \n")

xmlList = os.listdir(mdPath)
#xmlList = os.IterDir()(mdPath, recursive=FALSE)
for xml in xmlList:
    #xmlFile = open(mdPath+"/"+xml)
    lines = (open(mdPath+"/"+xml)).readlines()
    for line in lines:
        line = line.split(r" \n")
        line = str(line)
        try:
            #fnIndex = line.index("NAME")
            print(line.index("NAME"))
            print(line)
        except:
            #print(line)
            pass
# error of 'Permission Denied" for Revision History but that's fine because it'll end the loop for the project where it should anyway

