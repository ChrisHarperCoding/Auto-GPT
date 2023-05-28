import os

def is_directory_empty(directory):
    return len(os.listdir(directory)) == 0