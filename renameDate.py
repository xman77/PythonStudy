#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 01:40:28 2018

@author: nick
"""

import shutil,os,re

datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """,re.VERBOSE)
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo == None:
        continue

    beforPart = mo.group(1)
    monthPart = mo.group(2)
    dayPart   = mo.group(4)
    yearPart  = mo.group(6)
    afterPart = mo.group(8)
    
    euroFilename = beforPart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)
    
    print('Renaming "%s" to "%s".....' % (amerFilename,euroFilename))
    shutil.move(amerFilename,euroFilename)