#-*- coding: utf-8 -*-
#!D:\env\Scripts\MyProject\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyramid==1.4.5','console_scripts','pserve'
__requires__ = 'pyramid==1.4.5'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pyramid==1.4.5', 'console_scripts', 'pserve')()
    )
