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
        def filterFileList(self, files, fltr):
            res = []
            for f in files:
                if re.match(fltr, f):
                    res.append(f)
            return res
                    
        fltr = r"\w+\.py"
        self.filelist = filterFileList(self, os.listdir(self.work))
    
    
        
    def getImportMapping(self):
        '''
        getImportMapping() --> dict {"file.py" : ["import1", "import2", ... ]}
        
        '''
        def extractImports(self, src):
            '''
            extractImports(src) --> list
            
            Takes path to source file and returns list of import strings.
            
            '''
            importStringList = []
            with open(src, 'r') as f:
                for string in f:
                    for fltr in filterList:
                        if re.match(fltr, string):
                            importStringList.append(string)
            return importStringList

        def processImportStringList(self, importStringList):
            for s in importStringList:
                temp = s.split(" ")
                if s[0] == "import":
                    if s[1].

                elif s[0] == "from":
                    pass
            
        mapDict = {pfile : extractImports(pfile) for pfile in self.filelist} 



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
    
