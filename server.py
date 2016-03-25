from flask import Flask, render_template, g, abort
from ete3 import Tree, TreeStyle, TextFace
import os

from davisputnam import main
from davisputnam import satisfiable

app = Flask(__name__)

@app.route("/")
def index():
    g.arguments = os.listdir("static/inputs")
    for i in range(0, len(g.arguments)):
        g.arguments[i] = g.arguments[i].split(".")[0]

    return render_template("index.html")

@app.route("/argument/<name>")
def argument(name):
    g.name = name
    argument_file = "static/inputs/%s.txt" % name
    g.argument_tree = "/static/outputs/%s.png" % name
    argument_tree = "static/outputs/%s.png" % name

    try:
        f = open(argument_file)  # open the file
    except:
        abort(404)

    g.premises = []
    g.conclusion = None

    for line in f:
        g.premises.append(line.strip())
    g.conclusion = g.premises[-1]
    g.premises = g.premises[:-1]

    stmt_set = main.open_argument(argument_file)
    print stmt_set
    g.sat, tree = satisfiable.satisfiable(stmt_set)

    # set teh tree style...
    ts = TreeStyle()
    # don't show the name of the leaf nodes (which are just a x/o for a open/closed branch) in the final graph
    ts.show_leaf_name = False

    for child in tree.traverse():
        # add a marker with the name of each node, at each node
        child.add_face(TextFace(child.name), column=0, position="branch-top")

    # render the file and save it
    tree.render(argument_tree, tree_style=ts, w=5000)

    return render_template("argument.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
