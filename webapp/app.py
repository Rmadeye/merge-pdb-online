from flask import Flask, make_response, request, render_template, Response, send_file
from src import patcher

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

    merger = patcher.Patcher()
    merger.patch(requested_rigid, requested_flex, 'result.pdb')

    return send_file('result.pdb', as_attachment=True)




if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
