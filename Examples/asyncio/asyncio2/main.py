import asyncio
from datetime import datetime
import logging
from timeit import default_timer

from aiofile import async_open
import httpx
import requests

from asyncduration import async_timed
from asynclogging import async_logging_to_file
from authentication import watcher, get_api_key  # real key from www.pexels.com/uk-ua/api/ after registration


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

URL = 'https://api.pexels.com/v1/search'
API_KEY = get_api_key()
sub_tasks = []
query = 'ice'
# new_tasks = []


@watcher
async def save_downloaded_data(file: str, data: requests.Response) -> None:
    if data.status_code == 200:
        async with async_open(file, 'wb') as afp:
            await afp.write(data.content)
        await async_logging_to_file(f'{file}\nPhoto saved: \t\t{datetime.now()}')
        # new_task = asyncio.create_task(async_logging_to_file(f'{file}\nPhoto saved: \t\t{datetime.now()}'))
        # new_tasks.append(new_task)


async def download_it(query: str, current_count: int) -> None:
    headers = {'Authorization': API_KEY}
    params = {
        'query': query,
        'per_page': 1,
        'page': current_count,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(URL, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for item in data['photos']:
                photo = item['src']['original']  # print(item['src']['original'])
                photo_name = photo.split('/')[-1]
                sub_task = asyncio.create_task(save_downloaded_data(photo_name, requests.get(photo)))
                sub_tasks.append(sub_task)
                await async_logging_to_file(f'{photo_name}\nCreated download task:\t{datetime.now()}')
                return photo_name

        else:
            print(f'{response.status_code=}, {response.json()=}')

    # print(f'{query} - - - - - - - {current_count}')
    

@async_timed()
async def main():
    # query = 'car'
    page_count = 10
    current_count: int = 0
    tasks = []
    while current_count < page_count:
        current_count += 1
        task = asyncio.create_task(download_it(query, current_count))
        tasks.append(task) 
    # print(f'{tasks=}')
    results = await asyncio.gather(*tasks, return_exceptions=True)  # if alert in some of corutine - other working
    for result in results:
        # print(f'{result=}')
        print(result)
    await asyncio.gather(*sub_tasks, return_exceptions=True) if sub_tasks else None
    # await asyncio.gather(*new_tasks, return_exceptions=True) if new_tasks else None


if __name__ == "__main__":
    asyncio.run(main())


# poetry add httpx



