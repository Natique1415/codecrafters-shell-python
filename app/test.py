import os


def file_autocomplete_list() -> list[str]:
    for filename in os.listdir("."):
        print(filename)


file_autocomplete_list()
