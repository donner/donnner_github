from com.android.monkeyrunner import MonkeyRunner as mr, MonkeyDevice as md, MonkeyImage as mi
#from datetime import datetime
import sys

#save log at 01_addcontacts.log
addlog=open("01_addcontacts.log","w")

def writelog(logstr):
    #print "%s: %s" % (datetime.now(),logstr)
    print logstr
    #addlog.writelines(datetime.now()+ ": " +logstr+"\n")

pck="com.android.contacts"
actvt=".activities.PeopleActivity"
compontName=pck+"/"+actvt

device=mr.waitForConnection()
if not device:
    writelog("can't connect to device")
    sys.exit()

writelog("connected to device, and launch contacts")

device.startActivity(component=compontName)
#device.startActivity(component="com.android.contacts/.activities.ContactEditActivity")

#tele num
mr.sleep(2)
device.touch(200,70,"DOWN_AND_UP")
mr.sleep(0.5)
device.type("115999999711")

mr.sleep(2)
pic1=device.takeSnapshot()
pic1.writeToFile("E:\pic1.png","png")
subp1=pic1.getSubImage((24,110,456,690))
subp1.writeToFile("E:\subp1.png","png")
writelog("search contact")


mr.sleep(3)
device.touch(30,70,"DOWN_AND_UP")
writelog("finish search")

mr.sleep(3)
device.touch(450,750,"DOWN_AND_UP")
writelog("click add contact button")

#click add contact
mr.sleep(2)
device.touch(10,220,"DOWN_AND_UP")
device.type("nokia")

#shorten sleep time to avoid prompt cover tele num field
mr.sleep(0.2)
device.touch(100,400,"DOWN_AND_UP")
device.type("15999999711")

mr.sleep(0.2)
device.touch(100,600,"DOWN_AND_UP")
device.type("15999@hello.com")

#finish666
mr.sleep(1)
device.touch(30,70,"DOWN_AND_UP")
writelog("save contact")

#save and back to contact list
mr.sleep(5)
device.touch(10,70,"DOWN_AND_UP")
writelog("return contacts menu")

mr.sleep(2)
device.touch(200,70,"DOWN_AND_UP")
mr.sleep(0.5)
device.type("115999999711")
mr.sleep(2)
pic2=device.takeSnapshot()
pic2.writeToFile("E:\pic2.png","png")
subp2=pic2.getSubImage((24,110,456,690))
subp2.writeToFile("E:\subp2.png","png")
writelog("search contact")

addlog.close()

if(subp2.sameAs(subp1,1.0)):
    print "fail to add contact"
else:
    print "add contact successfully"


