import os
import shutil

src = 'C:\\Windows\\System32\\actions-runner\\_work\\new\\'
dest = 'F:\\dest\\'

#src_files = os.listdir(src)

for root, dirs, files in os.walk(src):  
    for filename in files:
        full_file_name = os.path.join(root, filename)
        if (os.path.isfile(full_file_name)):
            if full_file_name.endswith('.yaml'):
                shutil.copy(full_file_name, dest)
