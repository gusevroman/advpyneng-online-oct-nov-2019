from pprint import pprint
import asyncio
from itertools import repeat

import yaml
import netdev
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import logging

logger = logging.getLogger('My Script')
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(logging.Formatter(
    '%(asctime)s - THREAD %(thread)d - %(levelname)s - %(message)s', datefmt='%H:%M:%S'))

logger.addHandler(console)


start_msg = '===> Connection to: {} function {}'
received_msg = '<=== Result from: {} function {}'



def connect_ssh_sync(device, command):
    logger.info(start_msg.format(device['host'], 'SHOW'))
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result

def connect_ssh_sync_config(device, commands):
    logger.info(start_msg.format(device['host'], 'CONFIG'))
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(commands)
    return result

async def send_show_command_to_devices(devices, command, executor=None):
    tasks = []
    for device in devices:
        loop = asyncio.get_running_loop()
        tasks.append(loop.run_in_executor(executor, connect_ssh_sync, device, command))
    result = await asyncio.gather(*tasks)
    return result

async def send_cfg_command_to_devices(devices, command, executor=None):
    tasks = []
    for device in devices:
        loop = asyncio.get_running_loop()
        tasks.append(loop.run_in_executor(executor, connect_ssh_sync_config, device, command))
    result = await asyncio.gather(*tasks)
    return result

async def main():
    #executor = ThreadPoolExecutor(max_workers=4)
    result1 = await send_show_command_to_devices(devices, 'sh run | i hostname')
    pprint(result1)
    result2 = await send_cfg_command_to_devices(devices, 'logging 1.1.1.1')
    pprint(result2)


if __name__ == "__main__":
    sync_only_devices = ['192.168.100.2']
    with open('devices_netmiko.yaml') as f:
        devices = yaml.safe_load(f)
    result = asyncio.run(main())
