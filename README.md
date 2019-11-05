Merge flexible residues and ligand pdb after docking with native protein!

syntax: python3 __main__.py -ir rigid.pdb -if flex.pdb #currently works only for files put in the main folder

-> flex.pdb must contain only one model, with ATOM not divided by REMARKS data (see /sample for an example)


output: /out directory
