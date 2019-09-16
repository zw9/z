#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:27:14 2019

@author: atang148
"""

#import re
import io
import glob

#!pwd

fn=  "weblist_inc.md"
encoding = 'utf-8'

g = io.open(fn, "w",encoding='utf-8')

fnmd1 = glob.glob('./**/*.htm*',recursive=True)
fnmd1.extend ( glob.glob('./**/*.txt',recursive=True))
fnmd1.extend ( glob.glob('./**/*.md',recursive=True))
fnmd1.extend ( glob.glob('./**/*.ipynb',recursive=True))
#display(fnmd)

for f in fnmd1:
    print ( '#### [' + f + ']' + '(' + f +')' + "\n")
    g.write( '#### [' + f + ']' + '(' + f +')' + "\n")

g.close()

        
