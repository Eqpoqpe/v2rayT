# -*- coding: UTF-8 -*-
# (C) Copyright 2020 FINTF C
# Written by Ryan William (eqpoqpe@gmail.com)

import subprocess
import re

module : bool = True

import os
__USERPATH = os.path.expandvars("$HOME") + "/.config"
__PROGRAMCONFIG = __USERPATH + "/v2rayTerminal"
__CONFIG = __PROGRAMCONFIG + "/User"
__PATCH = __PROGRAMCONFIG + "/patch"
__SUBSCRIPTIONPATH = __PROGRAMCONFIG + "/v2rayTerminal.sub"
__SERVERNODECONFIG = __PROGRAMCONFIG + "/v2rayTerminal.conf"
__SERVERNODECONFIG_B = __PROGRAMCONFIG + "/v2rayTerminal.conf.backup"

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
        import json
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
        import base64
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
                "add" : "",
                "port": "",
                "aid" : "",
                "id"  : ""
        }
        try:
            for get_key in NODE_CONFIG_FILE_KEYWORDS:
                if get_key == "port":
                    NODE_CONFIG_KEYWORDS[get_key] = int( \
                            server_list[checked_node_id : int][get_key])
                NODE_CONFIG_KEYWORDS[get_key] = server_list[checked_node_id][get_key]
        except KeyError:
            exit()
        ''' /usr/~/.config/v2rayTerminal/config.json '''
        tmp_config = _ropen_j(path_set)
        set_header = tmp_config["outbounds"]["settings"]["vnext"][0]
        set_header["address"] = NODE_CONFIG_KEYWORDS["port"]
        set_header["port"] = NODE_CONFIG_KEYWORDS["port"]
        set_header["users"][0]["alterId"] = NODE_CONFIG_KEYWORDS["aid"]
        set_header["users"][0]["id"] = NODE_CONFIG_KEYWORDS["id"]
        json.dump(tmp_config, open(config_file + "/config.json", "w"), indent=2)
        exit()

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

class _patch:
    __CALL_CONFIG_PATH : str = "/home/ryan/v2rayT/call_config.json"
    def __gset_rule(self, _dict=_ropen_j(__CALL_CONFIG_PATH)):
        rule_ob = {
                "_patch_s" : _dict["exchange_rule"],
        }
        return rule_ob

    def _call_m(self):
        pass

class _call_interface(_patch):
    ''' _patch call outside functions list -> _call_interface
        _basic in-build functions list -> _call_interface
        _patch will read exchange call rule, return ex call functions list
    '''

    def __inti__(interface):
        ''' copy ex call functions list '''
        interface.__funb = _basic().func_dict
        interface.__funr = _patch()._call_m()

    def _runle(interface):
        pass

    def __vif(interface) -> int:
        __defualt = len(interface.__funr)
        __vif_val = 0
        for get_key in interface.__funb:
            for _get_key in interface.__funb[__defualt][1]:
                if (get_key == _get_key):
                    __vif_val += 1
        if (__vif_val == __defualt):
            return 0
        else:   return -1
