from flask import Flask, request, render_template, send_file
from src import flex_prep, utils
import os

app = Flask(__name__)


@app.route('/')
def form():
    return render_template("index.html")


@app.route('/merge', methods=["POST"])
def merge():
    requested_rigid = request.files['rigid_pdb']
    requested_flex = request.files['flex_pdb']
    utilities = utils.Utilities()
    if not requested_rigid:
        return render_template("no_file.html")
    if not requested_flex:
        return render_template("no_file.html")
    if utilities.check_extensions(requested_rigid.filename):
        if utilities.check_extensions(requested_flex.filename):
            dfprep = flex_prep.tideTheModel()
            dfprep.parse_the_dock(requested_rigid, requested_flex)
            return send_file(os.path.dirname(app.root_path) + '/workdir/result.pdb', as_attachment=True), utilities.clean()
        else:
            return render_template("flex_error.html")
    else:
        return render_template("rigid_error.html")


class AbsPath:
    def main_cwd(self):
        return os.path.dirname(app.instance_path)


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
