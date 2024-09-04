from pathlib import Path


def read_lines_from_file(filepath: str | Path):
    with open(filepath, "r") as f:
        return f.readlines()
