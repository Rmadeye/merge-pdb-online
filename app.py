from flask import Flask, make_response, request


app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['pdb'])

# import seq_model_predict as smp
# smp.load_model()
from io import StringIO


def merge(rigid_pdb, flex_pdb):
    print(rigid_pdb, flex_pdb)
    return None



def validate_pdbs(rigid_pdb, flex_pdb):

    return None




@app.route('/')
def form():
    return """
        <!DOCTYPE html>
        <html>
        <head>
        <title>GrumPy Peptides</title>
           <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
            <script src="https://netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>   
                <meta name="viewport" content="width=device-width, initial-scale=1.0">    
        <style>
        .dropdown-menu{
            background-color: #C1E3C1;
            border: 1px solid #5CB85C;
        }
        .divider{
            border: 1px dashed #5CB85C;
        }
        body {
            background-image: url("static/background1.png");
            background-repeat:no-repeat;
            background-size:cover;
        }
        </style>
        </head>

        <body>
            <div style = "position:relative; right:180px>
            <div class="container">
            <div class="btn-group">

            <button type="button" class="btn btn-success">menu</button>
            <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <span class="caret"></span>
                <span class="sr-only"></span>            
            </button>

            <ul class="dropdown-menu">
                <li><a href="https://github.com/jludwiczak/GrumpyPeptide">####NONE#####</a></li>
                <li><a href="https://drive.google.com/file/d/1WQkDxyDTNj9qF7FGLSybS0tF_hqfdWIC/view">####none%%%%%</a></li>
            </ul>
            </div>      
            </div>

        <center>
            <h1>Merge rigid protein with flexible docking residues</h1>                
            <font size="+2">######</font>
            <br></br>
            <form action="/merge" method="post" enctype="multipart/form-data">
                <input type="file" name="rigid_pdb" />
                <input type="file" name="flex_pdb" />
            <input type="submit" name="submit_button" value="Merge files">
            
            </form>
            <br></br>
            <h3> Made by Rmadeye </h2>
        </center>
        </body>
        </html>
    """


@app.route('/predict', methods=["POST"])
def transform_view():

    return None


if __name__ == "__main__":
    # app.run()
    app.run('127.0.0.1', 5000, debug=False)
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=5000)
    # serve(app, host='127.0.0.1', port=5000)