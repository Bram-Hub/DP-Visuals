from flask import Flask, render_template, g
import os

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

    try:
        f = open(argument_file)  # open the file
    except:
        print "Could not open file: %s" % argument_file
        exit(1)

    g.premises = []
    g.conclusion = None

    for line in f:
        g.premises.append(line.strip())
    g.conclusion = g.premises[-1]
    g.premises = g.premises[:-1]

    print g.premises
    print g.conclusion


    return render_template("argument.html")

if __name__ == "__main__":
    app.run(debug=True)
