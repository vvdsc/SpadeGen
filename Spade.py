import aiohttp
import asyncio
import requests
import threading
from pystyle import *
import datetime
from random import choice
from datetime import datetime
import uuid
import colorama
import json
import os
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor
spade = """

┌┼┐┌─┐┌─┐┌┬┐┌─┐
└┼┐├─┘├─┤ ││├┤ 
└┼┘┴  ┴ ┴─┴┘└─┘
"""
lock = threading.Lock()
code = 0

def rn():
    t = datetime.now().strftime('%H:%M:%S:%f')[:-4]
    return f"{Fore.LIGHTBLACK_EX}{t}     {Fore.RESET}    |    "

def fetch():
    try:
        response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
        print(f"{rn()}[{Fore.RED}/{Fore.RESET}] Spade      |    Got Proxies")

        proxies = response.text

        with open('proxies.txt', 'w') as x:
            x.write(proxies)
        with open('proxies.txt', 'r') as file:
            proxy_list = [line.strip() for line in file if line.strip()]
        with open('proxies.txt', 'w') as omagad:
            omagad.write('\n'.join(proxy_list))
    except requests.RequestException as e:
        print(f"{rn()}[{Fore.RED}/{Fore.RESET}] Spade      | Couldn't fetch proxies. {e}")
        return []


def req1():
    while True:
        data = {"partnerUserId": "50b1bf177eca2a06f77680c1aa6277e1d5a44eb6d8b4a72545348e4828cf0753"}
        try:
            proxy = "http://"+choice(open("proxies.txt").read().splitlines())
            url = 'https://api.discord.gx.games/v1/direct-fulfillment'
            headers = {
                'authority': 'api.discord.gx.games',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json',
                'origin': 'https://www.opera.com',
                'referer': 'https://www.opera.com/',
                'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
            }
            data = {
                'partnerUserId': "50b1bf177eca2a06f77680c1aa6277e1d5a44eb6d8b4a72545348e4828cf0753"
            }
            res = requests.post(url, headers=headers, json=data, proxies={'http': proxy})

            try:
                jsn = res.json()
                token = jsn.get('token')
                with lock:
                    global code
                    code += 1
                    os.system(f'title Spade [*] Total codes made - {code}')
                    with open('codes.txt', 'a') as file:
                        file.write(f'https://discord.com/billing/partner-promotions/1180231712274387115/{token}\n')

                    print(f"{rn()}[{Fore.GREEN}>{Fore.RESET}] Spade      | Generated a new code ")
            except json.JSONDecodeError as e:
                print(f"{rn()}[{Fore.RED}/{Fore.RESET}] Spade      | Error {res}")

        except requests.RequestException as e:
            print(f"{rn()}[{Fore.RED}/{Fore.RESET}] Spade      | Couldn't generate a new code. {e}")


def req():
    x = int(input(f"{Fore.RED}[ Threads ] > {Fore.RESET}"))
    threads = []
    for _ in range(x):
        thread = threading.Thread(target=req1)
        thread.daemon = True 
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    os.system('cls')
    os.system('title Spade [*] Starting')
    print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(spade)))
    print('\n\n')
    fetch()
    req()
