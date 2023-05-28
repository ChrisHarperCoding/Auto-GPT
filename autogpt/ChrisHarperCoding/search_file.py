import os

path = input('Enter directory path: ')
filename = input('Enter filename: ')

for root, dirs, files in os.walk(path):
    for file in files:
        if file == filename:
            print(os.path.join(root, file))