# Copyright (C) 2020 FINTF
# Written by Ryan William (eqpoqpe@gmail.com)

''' base_b.func and patch.func > IMPORT.interface > damo_cil
    IMPORT > call way interface for damo_cil

    add subscription
    re subscription
    continue config node file & back_config node file
'''

def erron(paremeter=[]) -> int:
    if (len(paremeter) == 0):
        print("paremeter is null")
        return 0
    else:   return -1

try:
    from base_b import _call_interface
    ''' call way '''
except ModuleNotFoundError:
    pass