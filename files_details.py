import os
import time


def files_details(path):
    for f in os.listdir(path):
        if os.path.isfile(f):
            file_size = os.path.getsize(f)
            file_length = len(f)
            modification_time = os.path.getmtime(f)
            readable_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(modification_time))
            print(f"{f}\t{file_size}\t{file_length}\t{readable_time}")
files_details("/home/nizam/PycharmProjects/pythonProject")