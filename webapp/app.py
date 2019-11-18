from flask import Flask, make_response, request, render_template
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
    #rigid_content = requested_rigid.stream.reader().decode("utf-8")
    #flex_content = requested_flex.stream.reader().decode("utf-8")
    merger = patcher.Patcher()
    #output = merger.patch(rigid_content, flex_content, 'result.pdb')
    output = merger.patch(requested_rigid, requested_flex, 'result.pdb')
    response = make_response(output)
    #response.headers["Content-Disposition"] = "attachment; filename=result.pdb"

    return response




if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
