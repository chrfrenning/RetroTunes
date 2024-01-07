# RetroTunes
Utility to convert MP3 files to a format compatible with the Adafruit Walkmp3rson (https://learn.adafruit.com/walkmp3rson-personal-mp3-tape-player/overview)

## Preparing / Installation

1. Install Python
2. Run pip install -r requirements.txt to get required libs
3. Install ffmpeg and add it to your path (uses ffmpeg.exe in the ffpmeg/bin folder)

## Conversion

1. Put files in a subdirectory called 'Input'
2. Run the utility
3. Transfer all files from 'Output' to your Walkmp3rson
4. Enjoy

The script starts in your working directory, looking for a folder called "input". Put all the files you want converted there.
It will create a new directory called "output", where it stores all the converted files.
The utility extracts Artist and Title from metadata and uses it to build filenames (shortened to fit the screen)
All files are converted to mono, 22050, 128k, mp3

Warning! When running 'converter.py', all files in the ./output directory will be deleted as to avoid duplicates!
