#!/usr/bin/env python3

import asyncio
import logging
import aiohttp

logging.basicConfig(level=logging.INFO)

async def request_gruenbeck(id: int, url: str, code: int, params: str):
    payload = f"id={id}&show={params}&code={code:03d}~"
    logging.info(f"Sending request to {url} with payload: {payload}")
    
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
        try:
            async with session.post(url, data=payload) as response:
                logging.info(f"Response status: {response.status}")
                if response.status == 200:
                    result = await response.text()
                    logging.info(f"Response content: {result}")
                    if result != "<data><code>wrong</code></data>":
                        logging.info("Valid response received.")
                else:
                    logging.error(f"Error: Received HTTP {response.status}")
        except aiohttp.ClientError as e:
            logging.error(f"Connection error: {str(e)}")


async def main():
    url = "http://192.168.1.36/mux_http/"
    ids = [671, 672, 673]
    code = 142
    params = "D_A_1_7|D_A_1_1|D_A_1_4"

    tasks = [request_gruenbeck(id, url, code, params) for id in ids]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
