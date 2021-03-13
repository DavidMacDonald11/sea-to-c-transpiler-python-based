import os
import sys
from modules.transpiler import transpiler

def find_files(directory = "src"):
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            yield os.path.join(root, filename)

        for new_dir in dirs:
            yield from find_files(new_dir)

if __name__ == "__main__":
    src_dir = sys.argv[1]
    bin_dir = sys.argv[2]

    for file in find_files(src_dir):
        if file.endswith(".sea") or file.endswith(".hea"):
            print(f"Transpiling {file}...")
            transpiler.transpile(file, src_dir, bin_dir)
