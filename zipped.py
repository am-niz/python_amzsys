import zipfile
import os


def make_zip(zip_file_name, files):
    for file in files:
        if os.path.isfile(file):
            with zipfile.ZipFile(zip_file_name, "w") as f:
                f.write(file, os.path.basename(file))
                print("zipped")


make_zip("sip.zip", ["sample.txt", "file1.py", "file2.py"])
