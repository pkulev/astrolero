import os, sys
import pydot

#1) get list of .py files
#2) get import strings from each file
#3) map {file, list_of_imported_files}
#4) generate dot file
#5) load dot file and write png

class CImportGrapher(object):
    def __init__(self, work = "./"):
        self.work = work

    def getFileList(self):
        
        

graph = pydot.graph_from_dot_file("test.dot")
graph.write_png("out.png")
