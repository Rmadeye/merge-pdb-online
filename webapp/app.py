from flask import Flask, request, render_template, send_file
from src import flex_prep
import os,shutil

app = Flask(__name__)

@app.route('/')
def form():
    shutil.rmtree(os.path.dirname(app.root_path) + '\\workdir')
    return render_template("index.html")


@app.route('/merge', methods=["POST"])
def merge():
    requested_rigid = request.files['rigid_pdb']
    requested_flex = request.files['flex_pdb']
    """Dziala"""
    # merger = patcher.Patcher()
    # merger.patch(requested_rigid, requested_flex, 'result.pdb')
    # """Bedzie"""
    dfprep = flex_prep.tideTheModel()
    dfprep.parse_the_dock(requested_rigid, requested_flex)

    return send_file(os.path.dirname(app.root_path) + '\\workdir\\result.pdb', as_attachment=True)

class AbsPath:
    def main_cwd():
        return os.path.dirname(app.instance_path)

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
