import os


def file_autocomplete_list() -> list[str]:
    files = []
    for filename in os.listdir("."):
        files.append(filename)

    return files


print(file_autocomplete_list())
