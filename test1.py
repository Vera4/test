import os

buf = ''
# buf2= '' # Actually -- you are never using buf2, so we could remove it.
docnum=1

# I'm creating a directory called 'files', where we can save the parts of files.
# But you need to remove it before running.
os.mkdir('files')

with open ('Articles1.txt', 'r') as f:
    for line in f:
        buf+=str(line)
        if 'DOCUMENTS' in line:
            # This could cause issues later:
            #  - `filename` variable is first a string with the filename
            #  - then you assign the file object to the `filename` variable
            #  - it is a good habit to not overwrite variables unintentionally.
            # filename = 'file_%d.txt'%docnum
            # filename = open(r'files/FILE_%d.txt'%docnum, 'w')
            # =================================================
            filename = 'files/file_%d.txt'%docnum
            file_obj = open(filename, 'w')
            file_obj.write(buf)
            file_obj.write('===================================================')
            file_obj.close() # This is another good habit -- close files
                             # when you finish using them. Not serious if you don't
                             # but it can lead to funny strange behaviours.
            buf = ''
            docnum += 1
        # else:
            # buf2 += str(line)
