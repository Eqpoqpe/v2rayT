# Copyright (C) 2020 FINTF
# Written by Ryan William (eqpoqpe@gmail.com)

''' /etc/
       v2rayT/
         stable/..
         alpha/..
         IMPORT.py
         base.py
         demo_cli.py
'''

try:
    from src.base_b import module
    if bool(module):
        from base_b import _basic, _checkf
        from stable.patch_stable import *
    func_b.append(_basic)
    func_b.append(_checkf)
    # func_p.append()
except:
    print(0)
