import os
from glob import iglob
import numpy as np
import soundfile as sf
from progress.bar import ChargingBar
from folder import folder

file_list = [f for f in iglob(folder, recursive=True) if os.path.isfile(f)]

with ChargingBar('Processing', max=len(file_list)) as bar:
    for f in file_list:
        if f.lower().endswith('wav'):
            try:
                sound_file = sf.SoundFile(f)
            except:
                print('ERROR', f)
            else:
                if sound_file.subtype != 'PCM_16':
                    print(sound_file.subtype)
        bar.next()

