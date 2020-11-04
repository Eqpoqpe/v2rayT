#!/usr/bin/python3

import time
import sys
import os
import requests
import base64
import json
import subprocess
import re
import webbrowser

USERPATH = os.path.expandvars("$HOME") + "/.config"
PROGRAMCONFIG = USERPATH + "/v2rayTerminal"
# CONFIGFILESPATH = os.path.expandvars("$HOME") + "/.v2rayTerminal"
SUBSCRIPTIONPATH = PROGRAMCONFIG + "/v2rayTerminal.sub"
SERVERNODECONFIG = PROGRAMCONFIG + "/v2rayTerminal.conf"
SERVERNODECONFIG_B = PROGRAMCONFIG + "/v2rayTerminal.conf.backup"
CONFIG = PROGRAMCONFIG + "/User"

PATH_SET = (USERPATH, PROGRAMCONFIG,\
     SUBSCRIPTIONPATH, SERVERNODECONFIG, SERVERNODECONFIG_B, CONFIG)

class _basic:
    def AddSubscriptionURL (
    	self,
    	file_path : tuple
    ) -> "subscription_url":
        subscription_url = input("\nURL: ")
        ''' path file '''
        if (subscription_url == "path file"):
            file_path = str(input("PATH: "))
            with open(file_path, 'r') as original:
                subscription_url = original.read()
        getfile = open(file_path[2], "w+")
        getfile.write(subscription_url)
        getfile.close()
        return subscription_url
        
    def AddConfig (
    	self,
    	content,
    	file_path : tuple
    ) -> "config":
        config =str(base64.urlsafe_b64decode(content), encoding="utf-8")
        getfile =open(file_path[3], "w+")
        getfile.write(config)
        getfile.close()
        return config
        
    def ReadConfig(self, paremeter, file_path):
        if paremeter == 1:
            getfile = open(file_path[3], "r")
            self.config = getfile.read().strip()
            getfile.close()
            return self.config
        else:
            getfile_backup = open(file_path[4], 'r')
            self.config = getfile_backup.read().strip()
            getfile_backup.close()
            return self.config
        
    def LoadSubscriptionContent(self, subscription_url, paremeter, file_path):
        try:
            content = requests.get(subscription_url).content
            missingpadding = 4- len(content) % 4
            if missingpadding:
                content += b"=" *missingpadding
            if os.path.exists(file_path[4]):
                os.remove(file_path[4])
            return content
        except:
            print("\nAddress error please check it\n")
            if paremeter == 0:
                os.remove(file_path[2])
                os.remove(file_path[3])
            elif paremeter == 1:
                os.remove(file_path[2])
                os.rename(file_path[3], file_path[4])
            exit()

    def ServerNode(self, original_config):
        print("\033c\nNODE LIST\n" + '-'*60)
        server_list = str.encode(original_config).splitlines()
        # del some error null
        for get_list in server_list:
            if len(get_list) == 0:
                server_list.remove(get_list)
        for get in range(len(server_list)):
            server_node = json.loads(base64.b64decode(bytes.decode(server_list[get]).replace("vmess://", "")))
            print('[' + str(get) + ']' + server_node["ps"])
            print('-'*60)
            server_list[get] = server_node
        return server_list

    def SetConfigFile(self, server_list):
        checked_node_id = int(input("SERVER NODE NUMBER\n\n: "))
        get_path = input("SEVA FILE PATH: /")
        node_file_path = "/" + get_path
        with open(PROGRAMCONFIG + "/config.json", 'r') as original_config:
            CONFIG = json.load(original_config)
        NODE_CONFIG_FILE_KEYWORDS = {"add": "", "port": "", "aid": "", "id": ""}
        try:
            for get_key in NODE_CONFIG_FILE_KEYWORDS:
                if get_key == "port":
                    NODE_CONFIG_FILE_KEYWORDS[get_key] = int(server_list[checked_node_id][get_key])
                NODE_CONFIG_FILE_KEYWORDS[get_key] = server_list[checked_node_id][get_key]
        except KeyError:
            pass
        PARTY_DEFUALT_KEY = CONFIG["outbounds"][0]["settings"]["vnext"][0]
        CONFIG["outbounds"][0]["settings"]["vnext"][0]["address"] = NODE_CONFIG_FILE_KEYWORDS["add"]
        CONFIG["outbounds"][0]["settings"]["vnext"][0]["port"] = NODE_CONFIG_FILE_KEYWORDS["port"]
        CONFIG["outbounds"][0]["settings"]["vnext"][0]["users"][0]["alterId"] = NODE_CONFIG_FILE_KEYWORDS["aid"]
        CONFIG["outbounds"][0]["settings"]["vnext"][0]["users"][0]["id"] = NODE_CONFIG_FILE_KEYWORDS["id"]
        json.dump(CONFIG, open(node_file_path + "/config.json", "w"), indent=2)
        del NODE_CONFIG_FILE_KEYWORDS, CONFIG
        exit()

class filesys:
    def checkfiles(self, path):
        DEFUALT_USER = {"user_definition": [{"configuration_file_path": ""},{"proxy": [{"socks": {"listen": "","port": ""}},{"http": {"listen": "","port": ""}}]}]}
        settings = {"v2rayT": {"Settings": {"Logo": "on"},"Paremeter": {"SYS_1": 0,"SYS_1": 1}}}
        if not os.path.exists(path[1]):
            os.mkdir(path[1], mode=0o777)
        for get in (path[2], path[3]):
            if not os.path.exists(get):
                open(get, "w+")
        if not os.path.exists(path[5]):
            os.mkdir(path[5], mode=0o777)
        if not os.path.exists(path[5] + "/settings.json"):
            json.dump(settings, open(path[5] + "/settings.json", 'w'), indent=4)
        if not os.path.exists(path[5] + "defualt.json"):
        	json.dump(DEFUALT_USER, open(path[5] + "/defualt.json", 'w'), indent=4)
        if os.path.exists(path[4]):
            SYS_PARTY_VALUE_0 = 1
        else:
            SYS_PARTY_VALUE_0 = 0
        if os.path.exists(path[3]):
            SYS_PARTY_VALUE_2 = 1
        else:
            SYS_PARTY_VALUE_2 = 0
        original_config_path = sys.path[0] + "/config.json"
        if not os.path.exists(original_config_path):
            if not os.path.exists(original_config_path):
                SYS_VALUE_PATRY = 0
            else:
                SYS_VALUE_PATRY = 1
        else:
            if not os.path.exists(path[1] + "/config.json"):
                with open(original_config_path, 'r') as original_config:
                    CONFIG = json.load(original_config)
                json.dump(CONFIG, open(path[1] + "/config.json", 'w'), indent=4)
                SYS_VALUE_PATRY = 1
                del CONFIG
            else:
                SYS_VALUE_PATRY = 1
        with open(path[2], 'r') as GET_SUB_URL:
            subscription_url = GET_SUB_URL.read().strip()
        return SYS_PARTY_VALUE_0, SYS_PARTY_VALUE_2, SYS_VALUE_PATRY, subscription_url, path

    def paremeter(self, paremeter, path_short):
        if paremeter in "init":
            with open(path_short[5] + "/settings.json", 'r') as config:
                CONFIG = json.load(config)
            LOGO_X = CONFIG["v2rayT"]["Settings"]["Logo"]
            return LOGO_X
        elif paremeter in "on":
            with open(path_short[5] + "/settings.json", 'r') as config:
                CONFIG = json.load(config)
            CONFIG["v2rayT"]["Settings"]["Logo"] = "off"
            json.dump(CONFIG, open(path_short[5] + "/settings.json", "w"), indent=4)
        elif paremeter in "off":
            with open(path_short[5] + "/settings.json", 'r') as config:
                CONFIG = json.load(config)
            CONFIG["v2rayT"]["Settings"]["Logo"] = "on"
            json.dump(CONFIG, open(path_short[5] + "/settings.json", "w"), indent=4)

class user_panel(filesys, _basic):

    def __init__(self, INIT_STATUS_VALUE):
        subscription_url = INIT_STATUS_VALUE[3]
        while True:
            if not subscription_url:
                while True:
                    print("\033c")
                    self.PAREMETER = self.paremeter("init", INIT_STATUS_VALUE[4])
                    self.logo(self.PAREMETER)
                    OPTION_LIST = []
                    SYS_VALUE = 0
                    DEFUALT_VALUE = 0
                    if INIT[0] == 1:
                        MAX_OPTION = 4
                        DEFUALT_OPTION = [" Subscription URL\n", " About\n", " Continue <Backup>\n", " Preferences\n"]
                    else:
                        MAX_OPTION = 3
                        DEFUALT_OPTION = [" Subscription URL\n", " About\n", " Preferences\n"]
                    for get_value in range(1, (MAX_OPTION + 1)):
                        GET_STRING = "{}{}{}".format("[", get_value, "]")
                        OPTION_LIST.append(GET_STRING)
                    for get_list_string in OPTION_LIST:
                        OPTION_LIST[OPTION_LIST.index(get_list_string)] = get_list_string +  DEFUALT_OPTION[DEFUALT_VALUE]
                        DEFUALT_VALUE += 1
                    for GET_STRING in OPTION_LIST:
                        print(GET_STRING)
                    if MAX_OPTION == 3:
                        branch = input(": ")
                        if branch == '1':
                            subscription_url = self.AddSubscriptionURL(INIT_STATUS_VALUE[4])
                            self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url, SYS_VALUE, INIT_STATUS_VALUE[4]),\
                                    INIT_STATUS_VALUE[4])
                            break
                        elif branch == '2':
                            webbrowser.open("https://github.com/Eqpoqpe/v2rayT")
                        elif branch == '3':
                            self.preferences(INIT_STATUS_VALUE[4])
                    elif MAX_OPTION == 4:
                        branch = input(": ")
                        if branch == '1':
                            subscription_url = self.AddSubscriptionURL(INIT_STATUS_VALUE[4])
                            self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url, SYS_VALUE, INIT_STATUS_VALUE[4]),\
                                    INIT_STATUS_VALUE[4])
                            break
                        elif branch == '2':
                            webbrowser.open("https://github.com/Eqpoqpe/v2rayT")
                        elif branch == '3':
                            self.SetConfigFile(self.ServerNode(self.ReadConfig(0, INIT_STATUS_VALUE[4])))
                            break
                        elif branch == '4':
                            self.preferences(INIT_STATUS_VALUE[4])
            else:
                while True:
                    print("\033c")
                    self.PAREMETER = self.paremeter("init", INIT_STATUS_VALUE[4])
                    self.logo(self.PAREMETER)
                    SYS_VALUE = 1
                    option_point = ["[1] Resubscription\n", "[2] Refresh Config\n", "[3] Continue\n", "[4] Preferences\n"]
                    for get_point in option_point:
                    	print(get_point)
                    branch = input(": ")
                    if branch in '1':
                        subscription_url = self.AddSubscriptionURL(INIT_STATUS_VALUE[4])
                        self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url, SYS_VALUE, INIT_STATUS_VALUE[4]),\
                                INIT_STATUS_VALUE[4])
                        break
                    elif branch in '2':
                        self.config = self.AddConfig(self.LoadSubscriptionContent(subscription_url, SYS_VALUE, INIT_STATUS_VALUE[4]), \
                                INIT_STATUS_VALUE[4])
                        break
                    elif branch in '3':
                        self.SetConfigFile(self.ServerNode(self.ReadConfig(1, INIT_STATUS_VALUE[4])))
                        break
                    elif branch in '4':
                        self.preferences(INIT_STATUS_VALUE[4])

    def logo(self, paremeter):
        if paremeter == "on":
            for get in range(5):
                print(" "* 10, "{}{}{}{}{}".format(" " * (5 - get), "/", "_____", "/", (" "*get)) + '|')
                if get == 4:
                    print(" "*9, "{}{}{}{}{}".format(" " * (5 - get), "/", "     ", "/", (" " * get)) + ' |')
            print("\n")
            
    def user_options(run_mode):
        DEFUALT_OPTION_I = [" Subscription URL\n", " About\n", " Continue <Backup>\n", " Preferences\n"]
        DEFUALT_OPTION_S = [" Subscription URL\n", " About\n", " Preferences\n"]
        option_point_n = ["[1] Resubscription\n", "[2] Refresh Config\n", "[3] Continue\n", "[4] Preferences\n"]

    def preferences(self, path_short):
        print("\033c")
        self.logo(self.PAREMETER)
        OPTION_LIST = []
        LO = "[1] {} LOGO\n"
        if self.paremeter("init", path_short) == "on":
            OPTION_LIST.append(LO.format("OFF"))
            USER_SET_PAREMETER = "on"
        else:
            OPTION_LIST.append(LO.format("ON"))
            USER_SET_PAREMETER = "off"
        OPTION_LIST.append("[2] *CLEAN\n")
        for get_point in OPTION_LIST:
            print(get_point)
        branch = input(": ")
        if branch in '1':
            self.paremeter(USER_SET_PAREMETER, path_short)
            del USER_SET_PAREMETER, OPTION_LIST
        elif branch in '2':
            print("\033c")
            print("Warning: will delete all user config files,\nincluod subscription and server node config")
            care = input("\nGo on? [Yes] or [No]: ")
            if care in ["YES", "yes", 'Y', 'y']:
                os.remove(subscription_path)
                os.remove(server_node_config_path)
                exit()
        elif len(OPTION_LIST) == 3:
            if branch == '3':
                list_number = []
                for get in range(6):
                    get_string = str(get) + ".. "
                    list_number.append(get_string)
                output_string = ".. "
                for get_string in list_number:
                    output_string += get_string
                    print("\033c")
                    print("Press \"Ctrl + C\" to stop recover\n")
                    print(output_string)
                    time.sleep(1)
                os.remove(server_node_config_path)
                os.rename(server_node_config_backup, server_node_config_path)
                print("Done!")

if __name__ == "__main__":
    system_0 = filesys()
    INIT = system_0.checkfiles(PATH_SET)
    if bool(INIT) == True:
        user_0 = user_panel(INIT)
    else:
        print("filesystem has some error!")
