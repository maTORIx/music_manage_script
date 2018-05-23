import os
import sys
import shutil
import glob
from mutagen.easyid3 import EasyID3

def main():
    FILE_DIR = sys.argv[1]

    file_pathes = glob.glob(os.path.join(FILE_DIR, "**"), recursive=True);
    progress_count = 0
    for path in file_pathes:
        print(progress_count, "/", len(file_pathes))
        progress_count += 1
        if getExt(path) in ["mp3", "wma", "wav"]:
            setID3(path)

def getExt(path):
    return path.split(".")[-1]

def setID3(music_path):
    music_tags = EasyID3(music_path)
    path_array = music_path.split("/")
    music_tags["title"] = "".join(path_array[-1].split(".")[:-1])
    music_tags["album"] = path_array[-2]
    music_tags["artist"] = path_array[-3]
    music_tags["albumartist"] = path_array[-3]
    print(music_tags)
    music_tags.save()


main()
