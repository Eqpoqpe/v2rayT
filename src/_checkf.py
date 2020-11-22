# Written by Ryan William (l_.ll@hotmail.com)

class _checkf:
    def _chf_mk(self, path_set=_PATH_SET, DEFUALT : str="SET", *FF_LS) -> None:
        if (type(path_set) == tuple):
            if (DEFUALT == "SET"):
                if (len(FF_LS) == 2):
                    for get_tmp_path in path_set[0:FF_LS[0]]:
                        os.mkdir(get_tmp_path, mode=0o777)
                    for get_tmp_path in path_set[FF_LS[1]:]:
                        open(get_tmp_path, "w+")
                else:
                    # FF_LS.Lenght not full
                    pass
            elif (DEFUALT == "folder"):
                for get_tmp_path in path_set:
                    os.mkdir(get_tmp_path, mode=0o777)
            elif (DEFUALT == "file"):
                for get_tmp_path in path_set:
                    open(get_tmp_path, "w+")
        elif (type(path_set) == str):
            if (DEFUALT == "SET"):
                # option error
                exit()
            elif (DEFUALT == "folder"):
                os.mkdir(path_set, mode=0o777)
            elif (DEFUALT == "file"):
                open(path_set, "w+")

    def _chf_exis(self, path, path_set=_PATH_SET, paremeter : str=None) -> list or int:
        if (path_set != __PATH_SET):
            if (os.exists(path)):   return (0)
            else:   return (1)
        elif (path_set == __PATH_SET):
            no_exs : list = []
            for get_tmp_path in path_set:
                if (not os.exists(get_tmp_path)):
                    no_exs.append(get_tmp_path)
                continue
            if (paremeter == 'l'):
                if (len(no_exs) != 0):
                    return (no_exs)
                else:   return (0)
            else:
                if (len(no_exs) != 0):
                    return (1)
                else:    return (0)
