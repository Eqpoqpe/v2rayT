# Written by Ryan William (eqpoqpe@gmail.com)

try:
    from base_b import _call_interface
except ModuleNotFound:
    exit()

if __name__ == "__main__":
    ''' Add subscription url
        Resubscription url, when can't content url, \
                will make a backup for older config file
        Continue
        Continue read backup file
    '''
    func = _call_interface().gfunc()
