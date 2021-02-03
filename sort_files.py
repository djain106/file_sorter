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
file_types = ['/exe', '/doc', '/pdf', '/images',
              '/misc', '/zip', '/sheets', '/video', '/installers']

for ftype in file_types:
    if not os.path.exists(sort_path + ftype):
        os.makedirs(sort_path + ftype)

type_mappings = {'png': 'images', 'jpg': 'images', 'jpeg': 'images', 'pdf': 'pdf', 'exe': 'exe',
                 'doc': 'doc', 'docx': 'doc', 'zip': 'zip', 'rar': 'zip', 'mp4': 'video', 'msi': 'installers'}

for file_name in os.listdir(sort_path):
    extension = file_extension(file_name)
    folder_name = type_mappings.get(extension, None)
    old_path = [sort_path, file_name]
    if folder_name is None:
        continue
    new_path = [sort_path, folder_name, file_name]
    shutil.move("/".join(old_path), "/".join(new_path))

# Add feature for selecting more file types
new_file_type = input('What is the new file type? (None if no new file types)')
new_type = new_file_type.lower() != 'none'
while new_type:

    new_file_type = input(
        'What is the new file type? (None if no new file types) \n')
    new_type = new_file_type.lower() != 'none'
