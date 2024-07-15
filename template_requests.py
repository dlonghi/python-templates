#!/usr/bin/env python3.12

"""
python3.12 -m venv venv --upgrade-deps
source venv/bin/activate
pip3.12 install --no-cache-dir --upgrade pip setuptools wheel
pip3.12 install --no-cache-dir --upgrade requests

python3.12 main.py

"""


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


def main():
    ts = str(int(datetime.now().timestamp()))
    url = f"https://api.flightradar24.com/common/v1/airport.json?code=rao&plugin[]=&plugin-setting[schedule][mode]=departures&plugin-setting[schedule][timestamp]={ts}&page=1&limit=100&fleet=&token="

    print(url)

    h = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'Referer': 'https://www.flightradar24.com/',
        'Referrer-Policy': 'strict-origin-when-cross-origin'
    }

    #r = requests.post(zabbix_api_url, json=zjson, verify=False)
    r = requests.get(url, headers=h)
    print(r)
    print(r.text)
    j = r.json()
    print(json.dumps(j, indent=4))


    """
    for i in j["result"]:
        #print(i)
        hostid = i["hostid"]
        host = i["host"]
        #name = i["name"]
        #print('---------------------------------------')
        #print(host)
    """
    

if __name__ == "__main__":
    main()


app_end_time = datetime.now()
app_delta_time = app_end_time - app_start_time
app_finished_in = f"\n--- Finished in {app_delta_time.days} days, {app_delta_time.seconds // 3600} hours, {app_delta_time.seconds // 60 % 60} mins, {app_delta_time.seconds % 60} secs"
