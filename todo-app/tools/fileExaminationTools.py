from os.path import getsize

def determine_file_size(path_to_file: str) -> int:
    if getsize(path_to_file) == 0:
        return 0

    return -1
