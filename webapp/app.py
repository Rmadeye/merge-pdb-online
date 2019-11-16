from flask import Flask, make_response, request, render_template
from src import dataframe_prep

app = Flask(__name__)

def merge(rigid_pdb, flex_pdb):
    print(rigid_pdb, flex_pdb)
    return None

def validate_pdbs(rigid_pdb, flex_pdb):

    return None

@app.route('/')
def form():
    return render_template("index.html")


@app.route('/predict', methods=["POST"])
def transform_view():



if __name__ == "__main__":
    # app.run()
    app.run('127.0.0.1', 5000, debug=False)
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=5000)
    # serve(app, host='127.0.0.1', port=5000)