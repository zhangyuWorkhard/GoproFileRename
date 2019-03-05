import os
import sys
from nt import chdir

#path = os.path.dirname(os.path.abspath(__file__))
path = sys.argv[1]
print path
chdir(path)

fileList = os.listdir(path)
print fileList

for i in fileList:
    if (i.find('GH') == 0):
        newname = 'GH' + i[4:8] + i[2:4] +'.MP4'
        print newname
        os.rename(i, newname)    
