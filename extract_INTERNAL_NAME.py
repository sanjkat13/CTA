# get "INTERNAL_NAME" element from xml files

# folders completed:
    # Planning CTA Rail Station ADA Assessment_34
    # Improve BusTurnarounds Mad Aus Hal Wav Hal Bel Gnd Nor
    # Harrison Curve Realignment_7
    # Garfield Park n Ride
    # Design Traction Power Systemwide Upgrades and Improvements_37
    # Design Substations Farwell Armitage Hill BreakerRoom
    # Design Signals Orange Line and Loop Upgrades
    # Design Red Line WTA Wilson Station
    # Design Red Line Wilson Station Gerber Bldg Restoration
    # Design Red Line Loyola Station Improvements
    # Design Red Line Howard Station
    # Design Red Line Dan Ryan Initiative Bridges - PNetID3447
    # Design Red Line 95th Street Station Improvements
    # Design Red Blue Line Subway Escalators
    # Design Rail Stations Front Door Program
    # Design Rail Station PA Systems
    # Design Purple Line Viaducts Retaining Walls and Stations
    # Design CTA In House Design Engineering Projects
    # Design Bus Train Washers Ashland ForestGlen Rosemont Howard
    # Design Bus North Park Oil Water Separator
    # Design Bus 77th Street Bus Garage
    # Design Brown Line Substations_31
    # Design Brown Line Signals and Communications
    # Design Brown Line Paulina Southport Wellington Diversey
    # Design Brown Line Kimball Kedzie Francisco Rockwell Western
    # Design Brown Line Damen Montrose Irving Park Addison_33
    # Design Brown Line Construction Management_27
    # Design Brown Line Clark Junction
    # Design Brown Line Belmont Fullerton_5
    # Design Brown Line Armitage Sedgwick Chicago_6
    # Design Blue Line Des Plaines Rail Shop Upgrade
    # Design Blue Line Congress Dearborn Signal Systems_34
    # Design Block37 Tunnel Connection
    # Dan Ryan Initiative_Gensler - Stations
    # Dan Ryan Initiative 35th Sox Stationhouse
    # Dan Ryan Initiative - Substations
    # Dan Ryan Initiative - Stations
    # Dan Ryan Initiative - Infrastructure
    # CTALaw - Const - Bus Train Washers Forest Glen Rosemont Howard
    # CTA Program Wide_6
    # CTA Maintenance Infrastructure Projects
    # CTA Maintenance and Replacement Projects
    # Const Systemwide Communications Upgrade_9
    # Const Subway Emergency Exits
    # Const Subway Drainage Pumps_42
    # Const Roof Cumberland Station Project
    # Const Roof 54th Shop 63rd Racine
    # Const Roof 4 Substations Archer Skokie Pulaski Ridgeland
    # Const Red Line Way Finding
    # Const Red Line State Street Subway Tie Renewal
    # Const Red Line North Clybourn Refurbishment
    # Const Red Line Morse Granville Stations
    # Const Red Line Howard VPI Control Panels_8
    # Const Red Line Howard Station
    # Const Red Line Dan Ryan Track TP and Stations
    # Const Red Blue Lines Subway Escalator Replacement
    # Const Purple Line Main Street Viaduct
    # Const Purple Line Church Street Viaduct
    # Const Pink Line Paulina Connector
    # Const Loop Signals Upgrade
    # Const JOC 007 WH Wight Hill General Work Orders
    # Const JOC 007 WH Red Line Cermak Station_7
    # Const JOC 007 WH Kedzie Garage Boilers_36
    # Const JOC 007 WH Forest Glen Inspection Pits
    # Const JOC 007 PB System CCTV Security Cameras
    # Const JOC 007 PB Paul Borg General Work Orders_44
    # Const JOC 007 FHP North Park Garage Bus Plugins
    # Const JOC 007 FHP Midway Wheel Truing Pit
    # Const JOC 007 FHP Kedzie Garage RTUs
    # Const JOC 007 FHP FHPaschen General Work Orders
    # Const JOC 005 006 All General Work Orders CTA Use Only
    # Const Intergovernment Projects CTA Use Only
    # Const Green Line 63rd Lower Flammable Storage Building
    # Const Digital Advertising Contract System Rail_9
    # Const Digital Advertising Contract Phase 2
    # Const Digital Advertising Contract Bus
    # Const Digital Advertising Contract Brown Line Stations
    # Const DCKB37 TCS TPS Upgrades and Improvements
    # Const Bus Upgrade Ventilation at South Shops
    # Const Bus Turnaround at Navy Pier
    # Const Bus Turnaround at 79th and Western
    # Const Bus Train Washers Forest Glen Rosemont Howard_4
    # Const Bus RWCC North Park Oil and Water Separator
    # Const Bus North Park Garage OWS & Grit Removal



####-----------------------------------------------##
import os

# set up csv file to write in
########### **** change csv file name for folder ****

folderdir1 = os.listdir(r"Z:/cta-archives/")
folderdir =[]
for project in folderdir1:
    #print(project)
    



    if project == "01_CTA Archives - Shortcut" or "UM_ProjectNet Archive Access Quick Start_20150501.pdf":
        print("skip")
    else:
        folderdir.append(project)
        
for project in folderdir:

    subpath = r"Z:/cta-archives/" + project + "/Documents/Metadata"
    
    #csvfile = open(r"C:/Users/skatwala.int/OneDrive - Chicago Transit Authority/pnetmapping/testingdocs/new2/xmlINTERNALNAME_Const Bus North Park Garage OWS & Grit Removal.csv",'a')
    csvfile = open(r"C:/Users/skatwala.int/OneDrive - Chicago Transit Authority/pnetmapping/testingdocs/new2/" + project, 'a')
    csvfile.write("XMLfilename, INTERNAL_NAME, \n")
                

    # get basic directory list of metadata folder contents
    ############ **** change folder name ****
    #dirlist = os.listdir(r"Z:\cta-archives\Const Bus North Park Garage OWS & Grit Removal\Documents\Metadata")
    dirlist = os.listdir(subpath)
    # set up empty list
    xmllist = []

    # populate list of xml files
    for item in dirlist:
        if "xml" in item:
            xmllist.append(item)
    #print(xmllist)

    for xml in xmllist:
        ##### **** change file name for folder ****
        filepath = r"Z:/cta-archives/" + project + r"/Documents/Metadata/" + xml

        file = open(filepath)
        lines = file.readlines()
    ##    i = 0
    ##    index_list = []
        for line in lines:
            
            if "INTERNAL_NAME" in line:
                #print(line)
                intname = line.replace("<INTERNAL_NAME>","").replace("</INTERNAL_NAME>","")
                print(intname)
                writeline = str([xml,intname])
                csvfile.write(writeline)
                csvfile.write(',\n')
                #index_list.append(i+1)
           # i = i+1
       # print(index_list)

    ##    lines = file.seek(0)
    ##    for ind in index_list:
    ##        print(lines[ind])

    csvfile.close()
    print("done", filepath)
