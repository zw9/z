# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello")
import sys
help(sys)
import glob
fnmd = glob.glob('../**/*.md',recursive=True)
print(fnmd)
fnpy = glob.glob('../**/*.ipynb',recursive=True)
fnpy
