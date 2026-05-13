import os

PATH_DIRECTORY = os.environ.get("PATH").split(os.pathsep)

# print(os.listdir("C:\\Windows\\system32"))


def executable_autocomplete_list(command_name: str) -> list[str]:
    executables = []
    for directory in PATH_DIRECTORY:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                executables.append(filename)

    return executables


does_command_exist("helo")
