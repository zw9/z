import os
import string

import re
import io
import glob
import os

def filelist_by_ext(dirname):

    #dirname = os.environ['HOME'] + "/Public/z/rpt"
    os.chdir(dirname )
    #x=os.listdir(dirname)

    print(os.getcwd())
    os.chdir(dirname)
    print(os.getcwd())

    y = glob.glob(   '**/*.*', recursive=True)
    y.sort(key=lambda f: os.path.splitext(f)[1])
    extold=""
    fn_dtl="filelistbyext"

    gfn_dtl = io.open( fn_dtl + ".html", "w", encoding='utf-8')
    print(fn_dtl)
    a=0
    gfn_dtl.write('<table border=1><tr>')
    for k in y:
        a +=1
        fileName, fileExtension = os.path.splitext(k)
        if fileExtension != extold:
            #print (fileExtension)
            gfn_dtl.write('</tr><tr><td>' + fileExtension + '\n')
            a=1
        #print(os.path.basename(fileName).replace("-"," "),k)
        b = a % 5
        if b == 0:
            gfn_dtl.write('</td></tr><tr><td>')
            # print ( '#### [' + f + ']' + '(' + f +')' + "\n")
        gfn_dtl.write(' &nbsp; '  + ' <a href="' + k + '">' + os.path.basename(fileName).replace("-"," ") + '</a> &nbsp; | \n')
        extold=fileExtension

    gfn_dtl.write('</td></tr></table>')

    gfn_dtl.close()

filelist_by_ext(os.environ['HOME'] + "/Public/z/rpt")
filelist_by_ext(os.environ['HOME'] + "/Public/z/rptvi")
filelist_by_ext(os.environ['HOME'] + "/Dropbox")

    #dirname = os.environ['HOME'] + "/Public/z/rpt"

# %run ~/Dropbox/z/code/filelistbyext.py
