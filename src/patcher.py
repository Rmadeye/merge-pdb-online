from src.file_access import FileReader, FileWriter
import shutil
import os
import pandas

class Patcher:
    def patch(self, base_file: str, aux_file: str, out_file: str):
        base_atom_reader = FileReader(base_file)
        aux_atom_reader = FileReader(aux_file)
        output_writer = FileWriter(out_file)

        atoms = base_atom_reader.read()
        aux_atoms = aux_atom_reader.read()
        aalist = ['ALA', 'ARG','ASN','ASP','CYS','GLU','GLN','GLY','HIS',
                  'ILE','LEU','LYS','MET','PHE','PRO','SER',
                  'THR','TRP','TYR','VAL']

        for i in range(len(atoms)):
            atom = atoms[i]
            aux_atom = next(
                (x for x in aux_atoms if x.name == atom.name and
                 x.residue_sequence_number == atom.residue_sequence_number and
                 x.residue_type == atom.residue_type),
                None
            )

            if aux_atom != None:
                atom.x = aux_atom.x
                atom.y = aux_atom.y
                atom.z = aux_atom.z
                atoms[i] = atom

        ligs = [aux_atom for aux_atom in aux_atoms if 'd' in aux_atom.chain_identifier]
        output = atoms + ligs

        shutil.rmtree('./tmp/')
        for item in os.listdir('./'):
            if item.endswith('.merge'):
                os.remove(os.path.join('./', item))
        os.chdir("./out")
        output_writer.write(output)
        print("File successfully converted")

