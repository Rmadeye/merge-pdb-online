from src.patcher import Patcher
from src.dataframe_prep import data_prep
from src.flex_prep import tideTheModel
import argparse

inputdata = argparse.ArgumentParser(description= "Process docking files")

inputdata.add_argument('-ir','--rigid-pdb',nargs = '*',
                       help = "Input rigid pdb file", required = True,)
inputdata.add_argument('-if','--flex-pdb',nargs = '*',
                       help = "Input flexible pdb file", required = True)

args = inputdata.parse_args()

dfprep = tideTheModel()
dfprep.parse_the_dock(args.rigid_pdb[0], args.flex_pdb[0])
