#!/usr/bin/env python3

import aiohttp
import asyncio

async def test_connection():
    url = "http://192.168.1.36/mux_http/"
    code = 142
    payload = f"id=673&show=D_A_1_7&code={code:03d}~"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload) as response:
            print(await response.text())

asyncio.run(test_connection())