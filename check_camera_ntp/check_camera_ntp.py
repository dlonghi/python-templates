#!/usr/bin/env python3.12

#from datetime import datetime
#app_start_time = datetime.now()
#import sys
#import subprocess
#from pathlib import PurePath, Path
#import inspect
import os
from pathlib import PurePath, Path
import json
import urllib3
urllib3.disable_warnings()
import requests
import xmltodict

app_path = PurePath(__file__)
app_name = app_path.name
app_dir = str(app_path.parent)
os.chdir(app_dir)

import config

telegram_token = config.TELEGRAM_TOKEN
telegram_chat_id = config.TELEGRAM_CHAT_ID
telegram_base_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={telegram_chat_id}"

cameras = config.CAMERAS


def send_telegram_message(telegram_text):
    telegram_url = f"{telegram_base_url}&text={telegram_text}"
    telegram_response = requests.get(telegram_url)
    print(telegram_response)

def main():

    print(cameras)
    for camera in cameras:
        #print(c)
        hostname = camera['hostname']
        url = camera['url']

        xml = '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope"><s:Body xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><GetSystemDateAndTime xmlns="http://www.onvif.org/ver10/device/wsdl"/></s:Body></s:Envelope>'
        headers = {'Content-Type': 'application/xml'}
        r = requests.get(url, data=xml, headers=headers, verify=False)
        rxml = r.text
        xjson = xmltodict.parse(rxml)

        ntp_value = xjson['s:Envelope']['s:Body']['tds:GetSystemDateAndTimeResponse']['tds:SystemDateAndTime']['tt:DateTimeType']

        if ntp_value != 'NTP':
            telegram_message = f"Camera {hostname} NÃO está com NTP #Teste"
            send_telegram_message(telegram_message)
            print(ntp_value)


if __name__ == "__main__":
    main()


#app_end_time = datetime.now()
#app_delta_time = app_end_time - app_start_time
#app_finished_in = f"\n--- Finished in {app_delta_time.days} days, {app_delta_time.seconds // 3600} hours, {app_delta_time.seconds // 60 % 60} mins, {app_delta_time.seconds % 60} secs"

#cat <<'EOF' > /etc/cron.d/03-check-camera-ntp
#*/1 * * * * super /usr/bin/python3.12 /opt/RGRTech/scripts/check_camera_ntp.py  2>&1
#EOF
