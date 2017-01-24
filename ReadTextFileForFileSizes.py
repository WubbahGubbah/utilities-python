import os

fi = open("c:/temp/aerialcroppedsizes/aerialcroppedfilestest.txt","r")
fo = open("c:/temp/aerialcroppedsizes/aerialcroppedfilesizes.txt","w")

for line in fi:
  #print (line)
  values = line.split("\t")
  thepath = values[1]
  thepath = thepath.replace("\\","/")
  thepath = thepath.strip()
  print(thepath)
  if os.path.exists(thepath):
    print("-----")
    print(thepath)
    thesize = os.path.getsize(thepath)
    fo.write(values[0] + "," + thepath + "," + str(thesize) + "\n")
    fo.flush
  
fi.close()
fo.close()
print("done")
