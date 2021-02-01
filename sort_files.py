import os
sort_path = input('Please input the path of folder to sort: ')
print(os.listdir(sort_path))

# for file in os.listdir(sort_path):
# print(file)

file_types = ['\exe', '\doc', '\pdf', '\images']

for ftype in file_types:
    if not os.path.exists(sort_path + ftype):
        os.makedirs(sort_path + ftype)
