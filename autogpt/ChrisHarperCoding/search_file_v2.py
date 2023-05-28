import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('path', help='directory path')
parser.add_argument('filename', help='filename to search for')
args = parser.parse_args()

for root, dirs, files in os.walk(args.path):
    for file in files:
        if file == args.filename:
            print(os.path.join(root, file))