# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import sys
import glob
#import re
import io


fn=  "fn_inc.md"
g = io.open(fn, "w",encoding='utf-8')

fnmd = glob.glob('./**/*',recursive=True)
#fnmd.extend( glob.glob('./**/*.ipynb',recursive=True))
#display(fnmd)
#print(fnmd)
for e in fnmd:
    e_txt="#### [" + e +"]("+ e + ")\n"
    print(e_txt)
    g.write(e_txt )

g.close
