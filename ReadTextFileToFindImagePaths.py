import os
import string

fi = open("d:/temp/aerialPhotosIndexFiles/20160823.txt","r")
fo = open("d:/temp/aerialPhotosIndexFiles/filesfound16.txt","w")

thisrootpath = "\\\server\\folder\\scans"

for line in fi:
  #print (line)
  values = line.split("\t")
  thisindexid=values[0]
  thisfolder=values[1]
  thisfilename=values[2]
  
  thispath = os.path.join( thisrootpath ,thisfolder ,  thisfilename.rstrip().lstrip() + ".tif")
  print(thispath)
  
  if os.path.exists(thispath):
    print(thispath)
    fo.write(thisindexid + "," + thispath + "\n")
    fo.flush

#thepath = thepath.strip()


  
fi.close()
fo.close()
print("done")
