# -*- coding: utf-8 -*-
from docutils import nodes
import sphinx.writers.latex as latex

def setup(app):
    print 1
    #latex.LaTeXTranslator.default_elements["babel"] = '\\usepackage[english]{babel}'
    #latex.LaTeXTranslator.default_elements["inputenc"] = ''    
    
