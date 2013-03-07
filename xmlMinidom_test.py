#
#from xml.dom.minidom import DOMImplementation
from xml.dom.minidom import *
# implementation = DOMImplementation()
# print implementation.hasFeature("Core","2.0")
# print implementation.hasFeature("Events","2.0")
# print implementation._features

def search_by_traversal(node,name):
    if not node.childNodes:
		return
	for child in node.childNodes:
		if child.nodeType == Node.ELEMENT_NODE and child.tagName == name:
			print child.toxml()
		search_by_traversal(node,child)


dom1 = parse("all_testsuites.xml")
root = dom1.documentElement
childs = root.childNodes
search_by_traversal(root,"testsuite")

#print dom1.toxml()
