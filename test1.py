buf = ''
buf2= ''
docnum=1

with open ('Articles1.txt', 'r') as f:
    for line in f:
        buf+=str(line)
        if 'DOCUMENTS' in line:
            filename = 'file_%d.txt'%docnum
            filename= open(r'C:\Users\u1233929\.spyder-py3\Splitfiles\FILE_%d.txt'%docnum, 'w')
            filename.write(buf)
            filename.write('===================================================')
            buf = ''
            docnum += 1
        else:
            buf2 += str(line)
