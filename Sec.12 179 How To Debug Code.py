#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 179. How To Debug Code
# https://docs.python.org/3/library/pdb.html

# debugging

# linting

# IDE / editor

# read errors

# pdb

import pdb


def add(n1, n2):
    pdb.set_trace()
    return n1+n2


# example of pdb interaction
"""
> /home/alex/Dropbox/College/2020.07 Udemy Python/Sec.12 179 How To Debug Code.py(22)add()
-> return n1+n2
(Pdb) n1
4
(Pdb) n2
'sss'
(Pdb) n1+n2
*** TypeError: unsupported operand type(s) for +: 'int' and 'str'


(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) 

(Pdb) step
TypeError: unsupported operand type(s) for +: 'int' and 'str'
> /home/alex/Dropbox/College/2020.07 Udemy Python/Sec.12 179 How To Debug Code.py(22)add()
-> return n1+n2
(Pdb) 
"""

print(add(4, 'sss'))
