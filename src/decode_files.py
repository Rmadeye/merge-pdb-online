import re, os
from src.system_preparation import PDBQTprep
from webapp import app

class Decoder:
    def __init__(self):
        pass

    def bytes_to_pdb(self, rigidfile: str, flexfile: str) -> str:
        workdir = app.AbsPath()


        for line in flexfile:
            strline = str(line, 'utf-8')
            with open(workdir.main_cwd() + '/workdir/'+'flex.tmp.pdb', 'a+') as clnout:
                clnout.write(strline)

        for line in rigidfile:
            strline = str(line, 'utf-8')
            with open(workdir.main_cwd() + '/workdir/'+'rigid.tmp.pdb', 'a+') as rgout:
                rgout.write(strline)

        dfp = PDBQTprep(workdir.main_cwd() + '/workdir/rigid.tmp.pdb',
                                    workdir.main_cwd() + '/workdir/flex.tmp.pdb')

        return dfp.files_preparation()
