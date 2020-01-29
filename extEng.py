import os
#import codecs

rpath = "./subs/"
wpath = "./out/"
ext = ".srt"
file_list = os.listdir(rpath)

sub_list = [file for file in file_list if file.endswith(ext)]
print("files: {}".format(file_list))
print("files: {}".format(sub_list))

def extEng(fn,fn2):
    rf = open(fn,'r')
    wf = open(fn2,'w')
    while True:
        line = rf.readline()
        if not line: break
        #print(line[0])
        if((line[0]>='a' and line[0]<='z') or (line[0]>='A' and line[0]<='Z') ):
            wf.write(line)
    rf.close()
    wf.close()

for fn in sub_list:
    extEng(rpath+fn,wpath+"ext_"+fn)


