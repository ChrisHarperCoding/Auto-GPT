import os
import tarfile

folder_path = '/root/autogpt/auto_gpt_workspace/CompressGPT/Tests/Test1'

# Get the list of files in the folder
file_list = os.listdir(folder_path)

# Create a tar file
with tarfile.open('compressed_folder.tar.gz', 'w:gz') as tar:
    # Add each file to the tar file
    for file in file_list:
        tar.add(os.path.join(folder_path, file))

print('Compression complete.')