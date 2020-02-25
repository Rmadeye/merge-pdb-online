from src.file_access import FileReader, FileWriter


class Patcher:
    def patch(self, base_file: str, aux_file: str, out_file: str):
        base_atom_reader = FileReader(base_file)
        aux_atom_reader = FileReader(aux_file)
        output_writer = FileWriter(out_file)

        atoms = base_atom_reader.reader()

        aux_atoms = aux_atom_reader.reader()

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

        self.aalist = [' ALA', ' ARG',' ASN',' ASP',' CYS',' GLU',' GLN',' GLY',' HIS',
                  ' ILE',' LEU',' LYS',' MET',' PHE',' PRO',' SER',
                  ' THR',' TRP',' TYR',' VAL']
        hets = [aux_atom for aux_atom in aux_atoms if aux_atom.residue_type not in self.aalist]

        output = atoms + hets

        output_writer.write(output)
        return output


