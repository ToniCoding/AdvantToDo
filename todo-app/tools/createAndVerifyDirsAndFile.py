from pathlib import Path

def createFullPathWithFile(path: str, fileName: str) -> bool:
    try:
        path_to_file = Path(path) / fileName

        path_to_file.parent.mkdir(parents=True, exist_ok=True)
        path_to_file.touch()

        return True

    except (PermissionError, OSError, ValueError, TypeError) as e:
        print(f"Error creando el archivo: {e}")
        return False