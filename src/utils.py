import os
from webapp import webapp

class Utilities:
    def __init__(self):
        pass

    def clean(self):
        to_be_cleaned = webapp.AbsPath()
        folder = to_be_cleaned.main_cwd() + '/workdir'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        return None

    def check_extensions(self, filename):
        if any(filename.endswith(e) for e in ['.pdb', '.txt']):
            return True
