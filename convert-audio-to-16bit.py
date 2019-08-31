import os
from glob import iglob
import numpy as np
import soundfile as sf
from progress.bar import Bar
from folder import folder

file_list = [f for f in iglob(folder, recursive=True) if os.path.isfile(f)]
error_list = []
subtype = ''
is_write = False

with Bar('Processing', max=len(file_list)) as bar:
    for f in file_list:
        is_write = False
        if f.lower().endswith('wav'):
            try:
                sound_file = sf.SoundFile(f)
                subtype = sound_file.subtype
            except Exception as err:
                error_list.append(err)
            else:
                data, samplerate = sf.read(sound_file.name)

                if sound_file.subtype != 'PCM_16' and sound_file.subtype != 'PCM_U8':
                    subtype = 'PCM_16'
                    is_write = True

                if samplerate > 44100:
                    samplerate = 44100
                    is_write = True

                if is_write:
                    sf.write(sound_file.name, data, samplerate, subtype)
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
