# Import the necessary modules
import os
import sys

# Define the directory to analyze
folder_path = '<actual_directory_path>'

# Get the list of files in the directory
file_list = os.listdir(folder_path)

# Define the compression methods for each file type
compression_methods = {
    'txt': 'gzip',
    'csv': 'gzip',
    'json': 'gzip',
    'jpg': 'jpegoptim',
    'jpeg': 'jpegoptim',
    'png': 'jpegoptim',
    'mp4': 'ffmpeg',
    'avi': 'ffmpeg',
    'mov': 'ffmpeg',
    'zip': 'zip'
}

# Define the progress report function
def progress_report(file_name, file_size, compressed_size):
    percent = round((1 - (compressed_size / file_size)) * 100, 2)
    sys.stdout.write(f'Compressing {file_name}... {percent}% complete\r')
    sys.stdout.flush()

# Loop through each file in the directory
for file_name in file_list:
    # Get the full path of the file
    file_path = os.path.join(folder_path, file_name)
    
    # Determine the type of the file
    file_type = file_name.split('.')[-1]
    
    # Determine the size of the file
    file_size = os.path.getsize(file_path)
    
    # Determine the best compression method to use for the file
    compression_method = compression_methods.get(file_type, 'zip')
    
    # Compress the file using the selected compression method
    os.system(f'{compression_method} {file_path}')
    
    # Determine the size of the compressed file
    compressed_size = os.path.getsize(f'{file_path}.{compression_method}')
    
    # Provide a progress report
    progress_report(file_name, file_size, compressed_size)

# Print a message indicating that the compression process is complete
print('Compression complete.')