from flask import Flask, request, render_template, send_file
from src import flex_prep
import os,shutil

app = Flask(__name__)

def clean():
    folder = os.path.dirname(app.root_path) + '/workdir'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)

@app.route('/')
def form():
    return render_template("index.html")


@app.route('/merge', methods=["POST"])
def merge():
    requested_rigid = request.files['rigid_pdb']
    requested_flex = request.files['flex_pdb']
    dfprep = flex_prep.tideTheModel()
    dfprep.parse_the_dock(requested_rigid, requested_flex)

    return send_file(os.path.dirname(app.root_path) + '/workdir/result.pdb', as_attachment=True), clean()

class AbsPath:
    def main_cwd():
        return os.path.dirname(app.instance_path)

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
