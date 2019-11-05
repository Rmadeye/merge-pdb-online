import string
class Atom:
    def __init__(self, row: str):
        self.serial_number = row[6:11]
        self.name = row[11:16]
        self.residue_type = row[16:20]
        self.chain_identifier = row[20:22]
        self.residue_sequence_number = row[22:26]
        self.x = row[31:38]
        self.y = row[39:46]
        self.z = row[47:55]
        self.occupancy = row[56:60]
        self.temperature_factor = row[61:66]
        # self.segment_identifier = row[73:76]
        self.element_symbol = row[77:79]
    def __str__(self):
        values = [
            "ATOM  ",
            self.serial_number.rjust(5),
            self.name.rjust(5),
            self.residue_type.rjust(4),
            self.chain_identifier.rjust(2),
            self.residue_sequence_number.rjust(4),
            self.x.rjust(12),
            self.y.rjust(8),
            self.z.rjust(9),
            self.occupancy.rjust(5),
            self.temperature_factor.rjust(5),
            # self.segment_identifier.rjust(4),
            self.element_symbol.rjust(13)
        ]
        return "".join(values)
