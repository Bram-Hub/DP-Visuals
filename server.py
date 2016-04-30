from flask import Flask, render_template, g, abort, request, flash, get_flashed_messages
from flaskext.markdown import Markdown
from ete3 import Tree, TreeStyle, TextFace
from PIL import Image, ImageDraw
import sys
import os

from davisputnam import main
from davisputnam import satisfiable
from davisputnam import parse

app = Flask(__name__)
app.secret_key = "$3cR3t"
app.debug = True
markdown = Markdown(app, safe_mode=True, output_format='html5')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        premises = []
        conclusion = None
        title = None

        for key in request.form:
            if key == "conclusion":
                if request.form[key] == "":
                    flash("Conclusion can't be empty!", "error")
                else:
                    conclusion = request.form[key]
                    parsed = parse.parse(conclusion)
                    if parsed is None:
                        flash("Coundn't parse conclusion: %s" % conclusion, "error")
            elif key == "title":
                if request.form[key] == "":
                    flash("Title can't be empty!", "error")
                else:
                    existing_arguments = os.listdir("static/inputs")
                    title = request.form[key].strip().replace(" ", "_") + ".txt"
                    if title in existing_arguments:
                        flash("An argument with this name already exists!", "error")
            else:
                if request.form[key] != "":
                    premise = request.form[key]
                    parsed = parse.parse(premise)
                    if parsed is None:
                        flash("Couldn't parse premise: %s" % premise, "error")
                    else:
                        premises.append(premise)

        if len(get_flashed_messages()) == 0:
            f = open("static/inputs/" + title, 'w')
            for premise in premises:
                f.write(premise + "\n")
            f.write(conclusion + "\n")
            f.close()

    # load all of the existing arguments
    g.arguments = sorted(os.listdir("static/inputs"))
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

    existing = os.listdir("static/outputs")
    for f in existing:
        if f == name + ".png":
            return render_template("argument.html")

    # set teh tree style...
    ts = TreeStyle()
    # don't show the name of the leaf nodes (which are just a x/o for a open/closed branch) in the final graph
    ts.show_leaf_name = False

    for child in tree.traverse():
        # add a marker with the name of each node, at each node
        child.add_face(TextFace(child.name), column=0, position="branch-top")

    # render the file and save it
    tree.render(argument_tree, tree_style=ts, w=5000)

    # crop out the unwanted part of the image...
    im = Image.open(argument_tree)
    (x, y) = im.size

    draw = ImageDraw.Draw(im)
    draw.rectangle((0, y*.5, x*.25, y), fill="white")
    im.save(argument_tree, "PNG")

    return render_template("argument.html")


@app.route("/about/")
def about():
    readme = open("README.md", "r").read()
    return render_template("about.html", readme=readme)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    port = None
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    app.run(host='0.0.0.0', port=port, processes=4)
