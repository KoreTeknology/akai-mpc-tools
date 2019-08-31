import os
from glob import iglob
from folder import folder

rootdir_glob = folder
file_list = [f for f in iglob('**/*', recursive=True) if os.path.isfile(f)]

for f in file_list:
    print(f)