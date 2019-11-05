import io
from src.model import Atom
from typing import List


class FileReader:
    def __init__(self, filename: str):
        self.filename = filename

    def read(self) -> List[Atom]:
        atoms = []

        with io.open(self.filename) as file:
            for row in file:
                atom = Atom(row)
                atoms.append(atom)

        return atoms


class FileWriter:
    def __init__(self, filename: str):
        self.filename = filename

    def write(self, atoms: List[Atom]):
        with io.open(self.filename, "x") as file:
            for atom in atoms:
                file.write(f"{atom}\n")
