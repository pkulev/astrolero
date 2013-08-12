import os, sys
import re
import pydot


#1) get list of .py files
#2) get import strings from each file
#3) map {file, list_of_imported_files}
#4) generate dot file
#5) load dot file and write png

class CImportGrapher(object):
    def __init__(self, work = "./"):
        self.work = work
        self.filelist = None

    def getFileList(self):
        def filterFileList(self, l, fltr):
            res = []
            for i in l:
                if re.match(fltr, i):
                    res.append(i)
            return res
                    
        fltr = r"\w+\.py"
        self.filelist = filterFileList(self, os.listdir(self.work))

    def getImportMapping(self):

#graph = pydot.graph_from_dot_file("test.dot")
#graph.write_png("out.png")

if __name__ == "__main__":
    work = "/home/most/programming/projects/pygame-study/spacegame/sources/"
    ig = CImportGrapher(work)
    ig.getFileList()
    ig.getImportMapping()
    #ig.generateDotFile()
    #ig.readDotFile()
    #ig.writePNG()
    
