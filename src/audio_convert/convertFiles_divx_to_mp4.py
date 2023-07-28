import ffmpeg
import os
import subprocess

# curdir = os.getcwd()
file_in = "T:\\The New Yankee Workshop\Season 4\\the_new_yankee_workshop_s04e13.divx"
file_out = "T:\\The New Yankee Workshop\Season 4\\the_new_yankee_workshop_s04e13.mp4"

subprocess.call(['ffmpeg', '-i', file_in, '-acodec', 'aac', '-vcodec', 'libx264', file_out])

# filenames = []
# print("Hello")
# for (dirpath, dirnames, filenames) in os.walk(curdir):
#     for file in filenames:
#         print(os.path.join(curdir, file))
#         if '.divx' or '.avi' in file:
#             name, ext = os.path.splitext(file)
#             input = os.path.join(dirpath, file)
#             output = os.path.join(dirpath, name + '.mp4')
#             print("Converting %s to %s" % (input, output))
#             subprocess.call(['ffmpeg', '-i', input, '-acodec', 'aac', '-vcodec', 'libx264', output])
