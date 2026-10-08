import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(response.status)
        

async def main(): 
    url = ["https://httpbin.org/delay/5"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in url]
        await asyncio.gather(*tasks)
        
        
asyncio.run(main())              
        