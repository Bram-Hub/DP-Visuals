from ete3 import Tree, TreeStyle, TextFace

t = Tree("(a,b);")

# Basic tree style
ts = TreeStyle()
ts.show_leaf_name = False

# Creates two faces
hola = TextFace("hola")

for tree in t.traverse():
    tree.add_face(TextFace(tree.name), column=0, position="branch-top")


print t
t.show(tree_style=ts)
