from flask import Flask, make_response, request, render_template, Response, send_file
from src import patcher, dataframe_prep, flex_prep
import os

app = Flask(__name__)


def validate_pdbs(rigid_pdb, flex_pdb):

    return None

@app.route('/')
def form():
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

    return send_file('result.pdb', as_attachment=True)

class AbsPath:
    def main_cwd():
        return os.path.dirname(app.instance_path)



if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
