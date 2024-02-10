from pathlib import Path


def delete_tmp_file(filepath: str) -> None:
    """
    Delete the temporary file created for testing purposes.

    :param filepath: The file path to the temporary file.
    """
    path = Path(filepath)
    if path.exists():
        path.unlink()
