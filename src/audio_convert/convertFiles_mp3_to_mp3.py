import ffmpeg
import os
import subprocess

# curdir = os.getcwd()
curdir = "C:/Users/James/Downloads/Music/Hermano/[2002] Only A Suggestion"

filenames = []
for (dirpath, dirnames, filenames) in os.walk(curdir):
    for file in filenames:
        print(os.path.join(curdir, file))
        if '.mp3' in file:
            name, ext = os.path.splitext(file)
            file_in = os.path.join(dirpath, file)
            file_out = os.path.join(dirpath, f"{name}_converted.mp3")
            print("Converting %s to %s" % (file_in, file_out))
            subprocess.call([
                'ffmpeg',
                '-i',
                file_in, 
                '-acodec', 
                'libmp3lame', 
                '-aq', 
                '2',
                file_out
            ])
