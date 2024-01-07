# RetroTunes (C) Sebastian Humm (botsquarebot@gmail.com) and Christopher Frenning (christopher@frenning.com) 2023

print("RetroTunes MP3 Converter/0.1a")

from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TPE1, TIT2
import os
import re

def clean_filename(filename):
    # Define a string of invalid characters (you might need to add more)
    invalid_chars = r'/:?"<>|'

    # Replace each invalid character with an empty string
    for char in invalid_chars:
        filename = filename.replace(char, '')

    # Alternatively, using regular expressions to replace all invalid characters in one go
    filename = re.sub(r'[/:?"<>|]', '', filename)

    return filename

def convert_file(input_filename, output_filename):
    audio = AudioSegment.from_mp3(input_filename)
    audio = audio.set_frame_rate(22050)
    audio = audio-35
    mono = audio.set_channels(1)


    bitrate = "128k"
    mono.export(output_filename, format = "mp3", bitrate = bitrate)

def list_input_files():
    dir = os.path.join(".", "input")
    print(dir)
    files = os.listdir(dir)
    #print(files)
    for i in range(len(files)):
        files[i] = os.path.join(dir, files[i])
    return files

input_dir = ".\input"
if not os.path.exists(input_dir):
    os.makedirs(input_dir)

output_dir = ".\output" 
if os.path.exists(output_dir):
    for ef in os.listdir(output_dir):
        os.remove(os.path.join(output_dir,ef))
else:
    os.makedirs(output_dir)


counter = 0
for f in list_input_files():
    m = MP3(f, ID3 = ID3)
    artist = "Unknown Artist"
    title = "Unknown Title"

    if "TPE1" in m.tags:
        artist = m.tags["TPE1"].text[0]

    if "TIT2" in m.tags:
        title = m.tags["TIT2"].text[0]

    print("converting " + f + "...")
    print(artist, title)
    counter = counter + 1
    formatted_number = "{:02}".format(counter)
    o = formattednumber + "" + cleanfilename(artist[:16]) + "" + clean_filename(title[:16]) + ".mp3"
    print(o)

    convert_file(f, os.path.join(output_dir, o))
    print("Done")
