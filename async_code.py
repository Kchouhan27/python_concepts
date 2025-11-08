import asyncio
import aiohttp

API_URLS = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3",
    "https://jsonplaceholder.typicode.com/todos/4",
    "https://jsonplaceholder.typicode.com/todos/5",
]

async def fetch(session, url):
    """Single API call with error handling."""
    try:
        async with session.get(url, timeout=5) as response:
            if response.status != 200:
                return {"error": f"HTTP {response.status}", "url": url}

            return await response.json()  

    except Exception as e:
        return {"error": str(e), "url": url}

async def fetch_all_apis():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in API_URLS]
        return await asyncio.gather(*tasks)

async def main():
    print("Fetching 5 APIs at the same time...")
    results = await fetch_all_apis()
    for r in results:
        print(r)

asyncio.run(main())
