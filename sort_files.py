import os
import shutil
sort_path = input('Please input the path of folder to sort: ')
sort_path = sort_path.replace("\\", "/")

# Function to get file extension type


def file_extension(file_name):
    split_word = file_name.split(".")
    if len(split_word) == 1:
        return
    return split_word[-1]


# Folders to create/place into
file_types = ['\exe', '\doc', '\pdf', '\images', '\misc', '\zip']

for ftype in file_types:
    if not os.path.exists(sort_path + ftype):
        os.makedirs(sort_path + ftype)

type_mappings = {'png': 'images', 'jpg': 'images', 'jpeg': 'images', 'pdf': 'pdf', 'exe': 'exe',
                 'doc': 'doc', 'docx': 'doc', 'zip': 'zip', 'rar': 'zip'}

for file_name in os.listdir(sort_path):
    extension = file_extension(file_name)
    folder_name = type_mappings.get(extension, None)
    if folder_name is None:
        continue
    old_path = [sort_path, file_name]
    new_path = [sort_path, folder_name, file_name]
    shutil.move("/".join(old_path), "/".join(new_path))
