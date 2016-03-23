from ete3 import Tree, TreeStyle
t = Tree("((a,b),c);")
ts = TreeStyle()
ts.show_leaf_name = True
ts.rotation = 90

print t
print t.children

test = Tree()
test.name = "Test Test Test"
t.children.append(test)
print t

#t.render("node_style.png", w=400)
