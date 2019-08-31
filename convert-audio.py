import os
from glob import iglob
import numpy as np
import soundfile as sf
from progress.bar import Bar
from folder import folder

file_list = [f for f in iglob(folder, recursive=True) if os.path.isfile(f)]
error_list = []

with Bar('Processing', max=len(file_list)) as bar:
    for f in file_list:
        if f.lower().endswith('wav'):
            try:
                sound_file = sf.SoundFile(f)
            except Exception as err:
                error_list.append(err)
            else:
                if sound_file.subtype != 'PCM_16':
                    data, samplerate = sf.read(sound_file.name)
                    # sf.write(sound_file.name, data, samplerate, 'PCM_16')
            finally:
                sound_file.close()
        bar.next()

if error_list:
    print('Some error occured in the following files:')
    with open('error_logs.txt', 'w') as f:
        for item in error_list:
            f.write("%s\n" % item)
            print(item)
        f.close()

