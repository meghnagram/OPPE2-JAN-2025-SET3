img_extensions = {'jpg', 'jpeg', 'png', 'gif'}


import os

with open(filename) as f:
    total_size = 0
    for line in f:
        size, name = line.strip().split(',')
        size = int(size)
        if name.split('.')[-1].lower() in img_extensions:
            total_size += size
    print(total_size)

#Another Method:

img_extensions = {'jpg', 'jpeg', 'png', 'gif'}
# Write your code here, use the variable filename for the filename

with open(filename,'r') as file:
    sum=0
    for line in file:
        # dot=line.index('.')
        comma=line.index(',')
        # print
        ext=line[-5::]
        # print (ext)
        if ext.lower().strip() in ('.jpg','jpeg','.png','.gif'):
            # print("hello")
            sum += int(line[0:comma])
            
    print (sum)

Total Size of Image Files
Given a file containing file sizes and file names separated by a comma, find the total size of image files with extensions .jpg, .jpeg, .png, and .gif (case insensitive).

Assumptions

The file is in the standard format where each line has a file size followed by a file name.
The file size is in bytes.
The file name is in the format filename.extension.
Examples

Input File

2000,file1.jpg
890,file2.txt
30500,file3.JPEG
12000,file4.png
40000,file5.gif
490,file6.docx
Output

84500
Explanation

The total size of image files, which is 2000 + 30500 + 12000 + 40000 = 84500
