# Writtin by Ryan William (l_.ll@hotmail.com)

def _sipea(cpy_func_size) -> int:
    return cpy_func_size

def _sepods(cpy_func, set_ize) -> list or tuple:
    '''
    if (type(cpy_func) != tuple or dict):
        error()
    '''
    peapod = []
    set_ize += 1
    for lo_val in range(set_ize):
        if (lo_val == 0):
            peapod.append(cpy_func)
        else:   peapod += []
    return peapod

def _sepatch(peapod) -> dict or tuple:
    _isize = len(peapod) - 1 # pods index
    _csize = len(peapod[0]) # cpy_func index
    patch_pod = []
    for lo_val in range(_csize):
        if (lo_val > len(peapod[_isize]) - 1 or peapod[_isize][lo_val] == None):
            in_lo = _isize
            while (in_lo >= 0):
                if (lo_val > len(peapod[in_lo]) - 1 or peapod[in_lo][lo_val] == None):
                    in_lo -= 1
                else:
                    patch_pod.append(peapod[in_lo][lo_val])
                    in_lo = -1 # stop while loop
        else:   patch_pod.append(peapod[_isize][lo_val])
    return patch_pod
