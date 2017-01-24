import os
import sys
import xml.etree.ElementTree as ET
import datetime

rootdir = '//server/project/subfolder/In/'
rootdir = 'd:/temp/images/'
fo = open('d:/temp/opinionfolders.txt','w')

print(rootdir)

daysToGoBack = 14
deltaToGoBack = datetime.timedelta(days=daysToGoBack)

for root, dirs, files in os.walk(rootdir, topdown=False):
    for name in dirs:
        subDirPath = os.path.join(root, name)
        if ((datetime.datetime.today() - datetime.datetime.fromtimestamp(os.path.getmtime(subDirPath))) < deltaToGoBack):
		    #if the folder is in the date range
            if (os.path.isfile(os.path.join(subDirPath,'Props.xml'))):
			    #if the props.xml file exists
                print(subDirPath)
                tree = ET.parse(os.path.join(subDirPath,'Props.xml'))
                xmlroot = tree.getroot()
                thingy = xmlroot.find('entry')
                filelist=xmlroot.find('entry').attrib['Attachments']
                findfilelist=filelist.split(',')
                for findthisfile in findfilelist:
                    #print(findthisfile)
                    #change sdgfileprod to sdgreportstore
                    findthisfile = findthisfile.replace('findservername','replaceservername')
                    if not(os.path.isfile(findthisfile)):
                        fo.write(name + "," + findthisfile + "\n")
                        fo.flush
				
fo.close()
print("done")
