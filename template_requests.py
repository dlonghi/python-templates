#!/usr/bin/env python3.12

from datetime import datetime
app_start_time = datetime.now()
import sys
import subprocess
#from pathlib import PurePath, Path
import inspect
import json
import urllib3
urllib3.disable_warnings()
import requests

import config
zabbix_username = config.ZABBIX_USERNAME
zabbix_password = config.ZABBIX_PASSWORD
zabbix_api_url = config.ZABBIX_API_URL

telegram_

def main():
    zjson = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": zabbix_username,
            "password": zabbix_password},
        "id": 1
    }

    r = requests.post(zabbix_api_url, json=zjson, verify=False)
    j = r.json()
    #print(json.dumps(j,indent=4))
    ztoken = j["result"]


    # Query the Zabbix API
    zjson = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": "extend",
            "selectHostGroups": "extend",
            "filter": {
                "status": "0"
            }
        },
        "id": 2,
        "auth": ztoken
    }
    r = requests.post(zabbix_api_url, json=zjson, verify=False)
    j = r.json()


    for i in j["result"]:
        #print(i)
        hostid = i["hostid"]
        host = i["host"]
        #name = i["name"]
        #print('---------------------------------------')
        #print(host)

if __name__ == "__main__":
    main()


app_end_time = datetime.now()
app_delta_time = app_end_time - app_start_time
app_finished_in = f"\n--- Finished in {app_delta_time.days} days, {app_delta_time.seconds // 3600} hours, {app_delta_time.seconds // 60 % 60} mins, {app_delta_time.seconds % 60} secs"

