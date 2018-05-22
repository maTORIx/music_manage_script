from pydub import AudioSegment
from pydub.playback import play
import shutil
import glob
import sys
import os

def main():
    ImportDir = sys.argv[1]
    ExportDir = sys.argv[2]
    Ext = sys.argv[3]
    
    file_pathes = getMusicDirectory(ImportDir)
    file_length = len(file_pathes)
    export_count = 0
    for path in file_pathes:
        print(export_count, "/", file_length)
        export_count += 1
        
        if getExt(path) in ["mp3", "wma", "wav"]:
            music = parseMusic(path)
            music_export_path = getExportPath(ImportDir, ExportDir, path)
            exportAudio(music, Ext, music_export_path)
        elif os.path.isfile(path):
            export_path = getExportPath(ImportDir, ExportDir, path)
            os.makedirs(os.path.dirname(export_path), exist_ok=True)
            shutil.copy(path, export_path)


def getMusicDirectory(music_path):
    file_list = glob.glob(os.path.join(music_path, "**"), recursive=True)
    return file_list

def getExt(path):
    return path.split(".")[-1]

def getExportPath(import_dir, export_dir, music_path):
    if import_dir[-1] == "/":
        import_dir = import_dir[0:-1]
    export_music_path = music_path[len(import_dir) + 1:]
    return os.path.join(export_dir, export_music_path)

def parseMusic(path):
    audio = AudioSegment.from_file(path)
    return {
        "audio": audio,
        "path": path,
        "info": {}
    }

def exportAudio(music, ext="mp3", path="."):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    music["audio"].export(path, ext)

main()
