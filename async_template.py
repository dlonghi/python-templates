#!/usr/bin/env python3

from pathlib import PurePath, Path
import time
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import json
import asyncio

import config

program_start_time = datetime.now()

program_path = PurePath(__file__)
program_name = program_path.name
program_dir = str(program_path.parent)

TZ = config.TZ

def sync_func_sleep(amount):
  time.sleep(amount)


async def main():
    loop = asyncio.get_event_loop()
    amount_of_time = 3
    output_sync_func = await loop.run_in_executor(None, sync_func_sleep, amount_of_time)


if __name__ == "__main__":
    asyncio.run(main())

program_end_time = datetime.now()
program_delta_time = program_end_time - program_start_time
print(f"--- Program {program_name} took {program_delta_time}")
