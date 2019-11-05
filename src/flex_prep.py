import os
import re
import src.dataframe_prep

endtext= str('ENDMDL')
pat=re.compile(r"ENDMDL")


class tideTheModel:
    def __init__(self):
        pass

    def make_tmp_dir(self):
        if not os.path.exists('tmp'):
            os.makedirs('tmp')
        if not os.path.exists('out'):
            os.makedirs('out')


    def parse_the_dock(self, rigidfile: str, flexfile: str) -> str:
        tideTheModel.make_tmp_dir(self)
        dfp = src.dataframe_prep.data_prep()
        with open(flexfile, 'r') as sub:
            print("Processing file")
            for line in sub:
                with open(flexfile.strip('.pdb') + '_model_1.merge', 'a+') as clnout:
                    clnout.write(line)
                    if pat.search(line) != None:
                        break

        return dfp.read_and_correct(rigidfile, flexfile.strip('.pdb') + '_model_1.merge')
