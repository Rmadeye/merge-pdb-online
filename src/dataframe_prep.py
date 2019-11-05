from biopandas.pdb import PandasPdb
from src.patcher import Patcher

class data_prep:
    def __init__(self):
        pass

    def read_and_correct(self, basename: str, flexname: str) -> str:
        patcher = Patcher()
        rigid = PandasPdb().read_pdb(basename)
        flex = PandasPdb().read_pdb(flexname)
        rigid.df['ATOM']['segment_id'] = 'tmp'
        flex.df['ATOM']['segment_id'] = 'tmp'
        rigid.to_pdb(path='./tmp/%s' % basename,
                     records=['ATOM'],
                     gz=False,
                     append_newline=True)
        flex.to_pdb(path='./tmp/%s' % flexname,
                     records=['ATOM'],
                     gz=False,
                     append_newline=True)

        return patcher.patch('./tmp/%s' % basename, './tmp/%s' % flexname,
                             str(basename.rstrip('.pdb')) + '_' +
                             str(flexname.rstrip('.pdbqt')) + '_' +
                             "out.pdb")
