import io
from src.model import Atom
from typing import List


class FileReader:
    def __init__(self, files: str):
        self.files = files

    def reader(self) -> List[Atom]:
        atoms = []
        with open(self.files, 'r') as file:
            """Tutaj zamiana dekodowania"""
            for row in file:
                #stringrow = str(row, 'utf-8')
                #atom = Atom(stringrow)
                atom = Atom(row)
                atoms.append(atom)

        return atoms


class FileWriter:
    def __init__(self, filename: str):
        self.filename = filename

    def write(self, atoms: List[Atom]):
        with io.open(self.filename, "w") as file:
            for atom in atoms:
                file.write(f"{atom}\n")
