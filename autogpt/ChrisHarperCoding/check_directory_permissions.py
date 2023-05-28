import os

path = '/Users/chris/Documents/GitHub/Auto-GPT/Test2/Auto-GPT/autogpt/auto_gpt_workspace/'

if os.path.exists(path):
    if os.access(path, os.R_OK):
        print('Directory exists and is readable')
    else:
        print('Directory exists but is not readable')
else:
    print('Directory does not exist')