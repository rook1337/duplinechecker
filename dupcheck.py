import sys
# Using readlines()
file1 = open(str.strip(sys.argv[1]), 'r')
Lines = file1.readlines()
filetext1=""
duplines=[]
uniqlines=[]
linenum=0
linecount=[]
# Strips the newline character
for line in Lines:
    filetext1=line.strip()
    file2 = open(str.strip(sys.argv[2]), 'r')
    Lines1 = file2.readlines()
    linenum=linenum+1
# Strips the newline character
    for line2 in Lines1:
        filetext2=line2.strip()
        if filetext1==filetext2:
            duplines.append(filetext1)
            linecount.append(linenum)

            
newline=[]

print("Duplicate Lines found: "+str(len(linecount)))


linenum=0
for line in Lines:
    linenum=linenum+1
    if linenum in linecount:
        pass
    else:
        newline.append(str.strip(line))



for line in newline:
    f = open("newlines.txt", "a")
    f.write(line+"\n")
    f.close()
