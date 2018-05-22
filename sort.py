import shutil
import glob
import sys
import os

def main():
    IMPORT_DIR = sys.argv[1]
    EXPORT_DIR = sys.argv[2]
    REMOVE_EXT = sys.argv[3]

    file_pathes = glob.glob(os.path.join(IMPORT_DIR, "**"), recursive=True);
    for path in file_pathes:
        if getExt(path) == REMOVE_EXT:
            continue
        elif os.path.isfile(path):
            copyFile(path, getExportPath(IMPORT_DIR, EXPORT_DIR, path))

def getExt(path):
    return path.split(".")[-1]

def getExportPath(import_dir, export_dir, file_path):
    if import_dir[-1] == "/":
        import_dir = import_dir[0:-1]
    export_path = file_path[len(import_dir) + 1:]
    return os.path.join(export_dir, export_path)

def copyFile(import_path, export_path):
    os.makedirs(os.path.dirname(export_path), exist_ok=True)
    shutil.copy2(import_path, export_path)

main()
