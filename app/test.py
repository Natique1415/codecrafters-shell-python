import os

PATH_DIRECTORY = os.environ.get("PATH").split(os.pathsep)  # type: ignore


# our aim is to get the list of all executales presennt in the path directory
def executable_autocomplete_list() -> list[str]:
    executables = []
    for directory in PATH_DIRECTORY:

        if os.path.exists(directory):
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                    executables.append(filename)

    return executables


executable_autocomplete_list()
