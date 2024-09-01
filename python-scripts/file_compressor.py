# python-scripts/file_compressor.py

import zipfile
import sys

def compress_files(zip_name, files):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)

if __name__ == "__main__":
    zip_name = sys.argv[1]
    files = sys.argv[2:]
    compress_files(zip_name, files)
