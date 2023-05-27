#!/usr/bin/env python3

import asyncio
import time

import aiohttp


async def request_gruenbeck(id:int)-> None:
    # for code in range(108, 999):
    code = 142 # gültig für z.B. D_H_2
    url = f"http://192.168.1.36/mux_http/"
    payload=f"id={id}&show=D_D_1|D_D_2|D_A_1_1|D_A_1_2|D_A_2_2|D_A_3_1|D_A_3_2|D_Y_1|D_A_1_3|D_A_2_3|D_Y_5|D_A_2_1~"
    # payload=f"id={id}&show=D_K_19&code={code:03d}~"
    # payload=f"id={id}&show=D_Y_10_1|D_Y_10_2~"
    payload=f"id={id}&show=D_A_1_2|D_A_1_5~"
    print(f"\nBegin downloading {url}: {payload}")
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, data=payload) as response: 
                print(f"Status: {response.status}")
                if response.status == 200:
                    print("Content-type:", response.headers['content-type'])
                    result = await response.text()
                    print(result)
                    if result != "<data><code>wrong</code></data>":
                        print(30*"-")
        except aiohttp.ServerDisconnectedError as e:
            print('Connection Error', str(e))


async def main():
    await asyncio.gather(request_gruenbeck(671), request_gruenbeck(672))


if __name__ == "__main__":
    s = time.perf_counter()

    asyncio.run(request_gruenbeck(673))
    # asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f"Execution time: {elapsed:0.2f} seconds.")
