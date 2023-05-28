#!/usr/bin/env python

import os
import urllib.request

url = 'https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg'
filename = '/tmp/googlechrome.dmg'

urllib.request.urlretrieve(url, filename)

os.system('hdiutil attach ' + filename)

os.system('sudo cp -r /Volumes/Google\ Chrome/Google\ Chrome.app /Applications/')

os.system('hdiutil detach /Volumes/Google\ Chrome/')

os.remove(filename)
