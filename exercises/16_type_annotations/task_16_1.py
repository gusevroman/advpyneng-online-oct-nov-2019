# -*- coding: utf-8 -*-
"""
Задание 16.1

Написать аннотацию для функций send_show и send_command_to_devices:
аннотация должна описывать параметры и возвращаемое значение.

Проверить код с помощью mypy, если возникли какие-то ошибки, исправить их.

Для заданий в этом разделе нет тестов!
"""

from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import time
from itertools import repeat

import yaml
from netmiko import ConnectHandler, NetMikoAuthenticationException


def send_show(device_dict, command):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


def send_command_to_devices(devices, command, max_workers):
    data = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            data[device["host"]] = output
    return data


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    pprint(send_command_to_devices(devices, "sh ip int br"))
