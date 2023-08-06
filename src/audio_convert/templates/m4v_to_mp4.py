import ffmpeg
import os
import subprocess

# curdir = os.getcwd()
curdir = "T:\Rainbow_Brite"


for x in os.listdir(curdir):
    if x.endswith(".m4v"):
        print(x)        
        name, ext = os.path.splitext(x)
        input = os.path.join(curdir, x)
        output = os.path.join(curdir, name + '.mp4')
        print("Converting %s to %s" % (input, output))
        subprocess.call(['ffmpeg', '-i', input, '-c', 'copy' , output])
