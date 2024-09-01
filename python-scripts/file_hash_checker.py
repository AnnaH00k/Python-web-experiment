# python-scripts/file_hash_checker.py

import hashlib
import sys
import json

def compute_hash(file_path, algo='sha256'):
    hash_func = getattr(hashlib, algo)()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

if __name__ == "__main__":
    file_path = sys.argv[1]
    algo = sys.argv[2] if len(sys.argv) > 2 else 'sha256'
    file_hash = compute_hash(file_path, algo)
    print(json.dumps({'hash': file_hash}))
