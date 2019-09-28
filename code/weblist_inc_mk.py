#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %run /Users/atang148/Dropbox/z/code/weblist_inc_mk.py

"""
Created on Sun Sep 15 22:27:14 2019

@author: zzz

"""

import re
import io
import glob
import os

# !pwd

print(os.getcwd())
os.chdir("/Users/atang148/Dropbox/z/rpt")

fn = "weblist_inc.md"
print(fn)
encoding = 'utf-8'

g = io.open(fn, "w", encoding='utf-8')

fnhtml = "weblist_inc.html"
print(fnhtml)
encoding = 'utf-8'

gfnhtml = io.open(fnhtml, "w", encoding='utf-8')

fnmd1 = glob.glob('./**/*.htm*', recursive=True)
fnmd1.extend(glob.glob('./**/*.txt', recursive=True))
fnmd1.extend(glob.glob('./**/*.md', recursive=True))
# fnmd1.extend ( glob.glob('./**/*.ipynb',recursive=True))
# display(fnmd)
a=0
g.write('---')
gfnhtml.write('<table border=1><tr>')
foldercur=""
folderprev=""
for f in fnmd1:
    a +=1
    b = a % 5
    if b == 0:
        g.write('\n---\n')
        gfnhtml.write('</tr><tr>')
    foldercur=os.path.dirname(f)
    if folderprev != foldercur:
        g.write('\n---\n' + foldercur + ' \n')
        gfnhtml.write('</tr><tr><td>' + foldercur + '</td>\n')
        a=1
    # print ( '#### [' + f + ']' + '(' + f +')' + "\n")
    g.write('| #### [' + os.path.basename(f).replace("-"," ") + ']' + '(' + f + ')' + "")
    gfnhtml.write('<td><a href="' + f + '">' + os.path.basename(f).replace("-"," ") + '</a></td>\n')
    folderprev=foldercur

gfnhtml.write('</tr></table>')
g.write('</tr></table>')

g.close()
gfnhtml.close()
