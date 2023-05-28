import os

folder_path = '/path/to/folder'

if os.path.exists(folder_path):
    print('Folder exists')
else:
    print('Folder does not exist')