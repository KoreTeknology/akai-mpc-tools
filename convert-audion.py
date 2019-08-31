import os
from glob import iglob

rootdir_glob = '/Volumes/Untitled2/WORK/convert-audio/DrumSamples/**/*'
file_list = [f for f in iglob('**/*', recursive=True) if os.path.isfile(f)]

for f in file_list:
    print(f)