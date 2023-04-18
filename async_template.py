#!/usr/bin/env python

import sys
import os
import time
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import json
import asyncio

import config

program_start_time = datetime.now()
program_name = os.path.basename(__file__)

TZ = config.TZ

def sync_func_sleep(amount):
  time.sleep(amount)


async def main():
    loop = asyncio.get_event_loop()
    amount_of_time = 3
    output_sync_func = await loop.run_in_executor(None, sync_func_sleep, amount_of_time)

program_end_time = datetime.now()
program_delta_time = program_end_time - program_program_start_time
print(f"--- {program_name} took {program_delta_time}")
