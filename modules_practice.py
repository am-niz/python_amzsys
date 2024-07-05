import os
# def list_files_in_dir(path):
#     return [f for f in set(os.listdir(path)) if os.path.isfile(os.path.join(path,f))]
#
# result = list_files_in_dir("/home/nizam/PycharmProjects/pythonProject")
# print(result)

def count_file(path):
    count_file_dict = {}
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            ext = f.split(".")[-1]
            if ext in count_file_dict:
                count_file_dict[ext] = count_file_dict[ext] + 1
            else:
                count_file_dict[ext] = 1
    print(count_file_dict)

count_file("/home/nizam/PycharmProjects/pythonProject")

