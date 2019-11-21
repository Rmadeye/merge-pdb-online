from biopandas.pdb import PandasPdb
from src.patcher import Patcher
from webapp import app



class data_prep:
    def __init__(self):
        pass

    def read_and_correct(self, basename: str, flexname: str) -> str:
        workdir = app.AbsPath()
        patcher = Patcher()
        rigid = PandasPdb().read_pdb(basename)
        flex = PandasPdb().read_pdb(flexname)
        rigid.df['ATOM']['segment_id'] = 'tmp'
        rigid.df['ATOM']['element_symbol'] != 'H'
        flex.df['ATOM']['segment_id'] = 'tmp'
        flex.df['ATOM']['element_symbol'] != 'H'
        rigid.to_pdb(records=['ATOM'], path = workdir.main_cwd()+'/workdir/rigid.tmp.pdb',
                     gz=False,
                     append_newline=True)
        flex.to_pdb(records=['ATOM'], path = workdir.main_cwd()+'/workdir/flex.tmp.pdb',
                     gz=False,
                     append_newline=True)

        return patcher.patch(workdir.main_cwd() + '/workdir/rigid.tmp.pdb', workdir.main_cwd() +'/workdir/flex.tmp.pdb', workdir.main_cwd() + '/workdir/result.pdb')