# -*- coding: UTF-8 -*-
# (C) Copyright 2020 FINTF
# Written by Ryan William (eqpoqpe@gmail.com)

try:
    from _peapods import _sepods, _sepatch
    from _checkf import _checkf
    from alpha._interface import func_dict
    import subprocess
    import re
    import os
    import json
    import base64
except ModuleNotFoundError:
    print("Module Not Found")
    exit()

module : bool = True
__USERPATH = os.path.expandvars("$HOME") + "/.config"
__PROGRAMCONFIG = __USERPATH + "/v2T"
__CONFIG = __PROGRAMCONFIG + "/User"
__PATCH = __PROGRAMCONFIG + "/patch"
__SUBSCRIPTIONPATH = __PROGRAMCONFIG + "/sub.conf"
__SERVERNODECONFIG = __PROGRAMCONFIG + "/nodelist.conf"
__SERVERNODECONFIG_B = __PROGRAMCONFIG + "/nodelist.conf.bak"

_PATH_SET : tuple 
_PATH_SET = (
        __USERPATH,
        __PROGRAMCONFIG,
        __SUBSCRIPTIONPATH,
        __SERVERNODECONFIG,
        __SERVERNODECONFIG_B,
        __CONFIG
)

def _rwopen(path, mode ='r', wri_str : str = None) -> str or bool:
    with open(path, mode) as original:
        if (mode == 'r'):
            SUB_INT = original.read()
            original.close()
            return (SUB_INT)
        elif (mode == 'w'):
            original.write(wri_str)
            original.close()
            return (True)

''' only read json files
    not support write json file
'''
def _ropen_j(path, mode = 'r') -> dict:
    try:
        with open(path, 'r') as original:
            str_j = json.load(str_j)
            original.close()
            return (str_j)
    except:
        pass

''' HOW PATCH CALL
'''

class _basic:
    def __init__(self, *paremeter):
        self.func_dict = {
            "__add_subscription_url_r"    : self.__add_subscription_url_r,
            "__add_config"                : self.__add_config,
            "__read_config"               : self.__read_config,
            "__load_subscription_content" : self.__load_subscription_content,
            "__server_node"               : self.__server_node,
            "__set_config_file"           : self.__set_config_file
        }

    ''' call function
        in-build some function set for IMPORT

        init subscription
        re subscription
        continue config node file & back_config node file
    '''
    def _callfunc(self, paremeter : "paremeter only for dev, mode",\
            path : tuple or str, url : str=None) -> bool:
        set_paremeter = [
                0, # init add subscription url
                1, # resubscription url, content errror make back_config file
                2, # continue
                3  # continue read back config file
        ]
        if (paremeter in (set_paremeter[0], set_paremeter[1])):
            __add_config(
                    __load_subscription_content(__add_subscription_url_r(0 \
                            ,path_set, url), paremeter, path),
                    path
            )
        elif (paremeter in (set_paremeter[2], set_paremeter[3])):
            __set_config_file (
                    __server_node(__read_config(paremeter - 2)),
                    ch_number,
                    save_path
            )

    def __add_subscription_url_r(self, paremeter=0, url : str=None, \
            path_set : tuple or str=_PATH_SET) -> int or str:
        if (paremeter == 0):
            if (type(path_set) == tuple or list):
                _rwopen(path_set[2], 'w')
                return (url)
            elif (type(path_set) == str):
                    _rwopen(path_set, 'w')
                    return (url)
            else:   return (1)
        elif (paremeter == 1):
            if (type(path_set) == tuple or list):
                return (_rwopen(path_set[2], 'r'))
            elif (type(path_set) == str):
                return (_rwopen(path_set, 'r'))
            else:   return (1)

    def __add_config(self, content : str, file_path=_PATH_SET) -> str:
        config = str(base64.urlsafe_b64decode(content), encoding="utf-8")
        getfile = open(file_path[3], "w+")
        getfile.write(config)
        getfile.close()
        return (config)
        
    def __read_config(self, paremeter : int, file_path=_PATH_SET) -> str:
        if (paremeter == 0):
            config = _rwopen(file_path[3], 'r').strip()
            return (config)
        elif (paremeter == 1):
            get_backup = _rwopen(file_path[4], 'r').strip()
            return (get_backup)
        elif (paremeter == 2):
            ''' read config files '''
            pass
        
    def __load_subscription_content(self, subscription_url : str, \
            paremeter : int, file_path=_PATH_SET) -> str:
        try:
            import requests
            content = requests.get(subscription_url).content
            missingpadding = 4- len(content) % 4
            if missingpadding:
                content += b"=" *missingpadding
            if os.path.exists(file_path[4]):
                os.remove(file_path[4])
            return (content)
        except:
            if (paremeter == 0):
                os.remove(file_path[2])
                os.remove(file_path[3])
            elif (paremeter == 1):
                os.remove(file_path[2])
                os.rename(file_path[3], file_path[4])
            exit()

    def __server_node(self, original_config : str) -> list:
        server_list = str.encode(original_config).splitlines()
        for get_list in server_list:
            if (len(get_list) == 0):
                server_list.remove(get_list)
        for get in range(len(server_list)):
            server_node = json.loads(base64.b64decode( \
                    bytes.decode(server_list[get]).replace("vmess://", "")))
            print('[' + str(get) + ']' + server_node["ps"])
            print('-'*60)
            server_list[get] = server_node
        return (server_list)

    def __set_config_file(self, server_list : list, node_number : int, save_path) -> None:
        config_file = "/" + save_path
        NODE_CONFIG_KEYWORDS = {
                "add" : None,
                "port": None,
                "aid" : None,
                "id"  : None
        }
        try:
            for get_key in NODE_CONFIG_FILE_KEYWORDS:
                if get_key == "port":
                    NODE_CONFIG_KEYWORDS[get_key] = int( \
                            server_list[checked_node_id : int][get_key])
                NODE_CONFIG_KEYWORDS[get_key] = server_list[checked_node_id][get_key]
        except KeyError:
            exit()
        tmp_config = _ropen_j(path_set)
        set_header = tmp_config["outbounds"]["settings"]["vnext"][0]
        set_header["address"] = NODE_CONFIG_KEYWORDS["port"]
        set_header["port"] = NODE_CONFIG_KEYWORDS["port"]
        set_header["users"][0]["alterId"] = NODE_CONFIG_KEYWORDS["aid"]
        set_header["users"][0]["id"] = NODE_CONFIG_KEYWORDS["id"]
        json.dump(tmp_config, open(config_file + "/config.json", "w"), indent=2)
        exit()

class _patch:
    try:
        _CALL_PATCH_CONFIG = _PATH_SET[1] + "/parule.json"
    except FileNotFoundError:
        print("File Not Found: " + _CALL_PATCH_CONFIG)
        exit()

    def grule(self):
        # patch rule include replace sort
        rule_dict = _ropen_j(_CALL_PATCH_CONFIG)
        if (rule_dict["patch"]["status"]):
            msort     = rule_dict["patch"]["patch_msort"]
            func_info = rule_dict["patch"]["info"]
        else:   msort = False
        return (msort, func_info)

    def _sort(self, rule=grule()[0]):
        func = []
        if (rule[0]):
            for lo_str in rule[0]:
                if (lo_str in func_dict["stable"]):
                    func.append(func_dict[lo_str])
                else:   func.append(None)
            return func
        return func

class _call_interface(_patch, _basic, _checkf):
    def __init__(self):
        self.cpy_func = self.func_dict
        self.rfunc = _sepods(cpy_func, 2)
        self.rfunc[len(self.rfunc) - 1] = _patch()._sort()

    def gfunc(self):
        return _sepatch(self.rfunc)
