# -*- coding: utf-8 -*-
'''
Задание 11.2

Создать сопрограмму (coroutine) configure_devices. Сопрограмма
должна настраивать одни и те же команды на указанных устройствах с помощью asyncssh.

Параметры функции:

* devices - список словарей с параметрами подключения к устройствам
* config_commands - команды конфигурационного режима, которые нужно отправить

Функция возвращает список строк с результатами выполнения команды на каждом устройстве.
Запустить сопрограмму и проверить, что она работает корректно с устройствами
в файле devices.yaml и командами в списке commands.

При необходимости, можно использовать функции из предыдущих заданий.

Для заданий в этом разделе нет тестов!
'''
commands = ['router ospf 55',
            'auto-cost reference-bandwidth 1000000',
            'network 0.0.0.0 255.255.255.255 area 0']

