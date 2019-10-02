#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %run ~/Dropbox/z/code/filelist_mk.py

"""
Created on Sun Sep 15 22:27:14 2019

@author: zzz

"""

import re
import io
import glob
import os

# !pwd

def filelist_by_folder(pathstr):

    print(os.getcwd())
    os.chdir(pathstr)
    print(os.getcwd())

    fn_head = "filelistbyfolder.html"
    print(fn_head)

    gfn_head = io.open(fn_head, "w", encoding='utf-8')
    fnmd1 = os.listdir()
    for fn_dtl in fnmd1:
        if '.' not in fn_dtl:
            #print(fn_dtl)
            gfn_head.write('<li><a href="' + str(fn_dtl) + '.html">' + str(fn_dtl) + '</a></li>\n')
            gfn_dtl = io.open(fn_dtl + ".html", "w", encoding='utf-8')
            fnmd1 = glob.glob( fn_dtl + '/**/*.*', recursive=True)
            #fnmd1.extend(glob.glob(fn_dtl + '/**/*.txt', recursive=True))

            a=0
            gfn_dtl.write('<table border=1><tr>')
            foldercur=""
            folderprev=""
            for f in fnmd1[:100]:
                a +=1
                foldercur=os.path.dirname(f)
                if folderprev != foldercur:
                    gfn_dtl.write('</tr><tr><td>' + foldercur + '</td>\n')
                    a=1
                b = a % 5
                if b == 0:
                    gfn_dtl.write('</tr><tr>')
                # print ( '#### [' + f + ']' + '(' + f +')' + "\n")
                gfn_dtl.write('<td>'  + ' <a href="' + f + '">' + os.path.basename(f).replace("-"," ") + '</a> &nbsp; </td>\n')
                folderprev=foldercur

            gfn_dtl.write('</tr></table>')

            gfn_dtl.close()

    gfn_head.close()

filelist_by_folder(os.environ['HOME'] + "/Public/z/rpt")
filelist_by_folder(os.environ['HOME'] + "/Public/z/rptvi")
#filelist_by_folder(os.environ['HOME']  )
