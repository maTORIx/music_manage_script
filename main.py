from pydub import AudioSegment
from pydub.playback import play
import glob
import sys
import os

def main():
    ImportDir = sys.argv[1]
    ExportDir = sys.argv[2]
    Ext = sys.argv[3]
    MusicPath = getMusicDirectory(ImportDir)
    file_length = len(MusicPath)
    export_count = 0
    for path in MusicPath:
        print(export_count, "/", file_length)
        music = parseMusic(path)
        music_export_path = getExportPath(ImportDir, ExportDir, music["path"])
        exportAudio(music, Ext, music_export_path)

def getMusicDirectory(music_path):
    file_list = glob.glob(os.path.join(music_path, "*"), recursive=True)
    return file_list

def getExportPath(import_dir, export_dir, music_path):
    export_music_path = music_dir[0:len(import_dir) - 1]
    return os.path.join(export_dir, export_music_path)

def parseMusic(path):
    audio = AudioSegment.from_file(path)
    return {
        "audio": audio,
        "path": path,
        "info": {}
    }

def exportAudio(music, ext="mp3"):
    music["audio"].export(path, ext)

main()
