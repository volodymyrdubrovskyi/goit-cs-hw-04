from pathlib import Path

# Files list in directory (including sub-directories)
def create_files_list(path: Path):
    result = []
    try:
        for child in path.iterdir():
            if child.is_dir():
                subresult = create_files_list(child)
                for i in range(len(subresult)):
                    result.append(subresult[i])
            else:
                result.append(child)
    finally:
        return result

# Read the file
def read_file(filename: Path):
    with open(filename, 'r') as f:
        try:
            result = f.read()
        except:
            result = ""
        return result