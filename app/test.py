# import os


# def file_autocomplete_list() -> list[str]:
#     files = []
#     for entry in os.scandir("."):
#         if entry.is_file():
#             print(f"{entry.name} is a file ")
#             files.append(entry.name)
#         else:
#             full_path

#     # return files
#     print(files)


# # def nested_file_autocomplete_list() ->


# print(file_autocomplete_list())


# import os

# folder_path = "."
# file_paths = []

# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         # Join the folder path and file name to get the full path
#         full_path = os.path.join(root, file)
#         file_paths.append(full_path)

# for file in file_paths:
#     file.replace("\\\\", "\\")
#     file.replace(".", "", 1)
#     print(file)
# print(file_paths)


import os

# def file_autocomplete_list() -> list[str]:
#     files_items = []
#     for root, dirs, files in os.walk("."):
#         for filename in files:
#             # Get the full path and convert it to a relative path
#             relative_path = os.path.relpath(os.path.join(root, filename), ".")
#             # print(f"Name: {filename} | Relative Path: {relative_path}")
#             files_items.append(relative_path)


#     return files_items
def file_autocomplete_list() -> list[str]:
    files_items = []
    for root, dirs, files in os.walk("."):
        for filename in files:
            # Get the full path and convert it to a relative path
            relative_path = os.path.relpath(os.path.join(root, filename), ".")
            # print(f"Name: {filename} | Relative Path: {relative_path}")
            files_items.append(relative_path)

    # return files_items
    # return [item.replace("\\\\", "\\") for item in files_items]
    # for items in files_items:
    #     print(items)

    return files_items


print(file_autocomplete_list())
