import re, os
import src.dataframe_prep
from webapp import app

endtext= str('ENDMDL')
pat=re.compile(r"ENDMDL")

class tideTheModel:
    def __init__(self):
        pass

    def parse_the_dock(self, rigidfile: str, flexfile: str) -> str:
        dfp = src.dataframe_prep.data_prep()
        workdir = app.AbsPath()
        for line in flexfile:
            strline = str(line, 'utf-8')
            with open(workdir.main_cwd() + '/workdir/'+'flex.tmp.pdb', 'a+') as clnout:
                clnout.write(strline)
                if pat.search(strline) != None:
                    break

        for line in rigidfile:
            strline = str(line, 'utf-8')
            with open(workdir.main_cwd() + '/workdir/'+'rigid.tmp.pdb', 'a+') as rgout:
                rgout.write(strline)

        return dfp.read_and_correct(workdir.main_cwd() + '/workdir/rigid.tmp.pdb',
                                    workdir.main_cwd() + '/workdir/flex.tmp.pdb')
