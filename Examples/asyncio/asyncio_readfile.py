import asyncio
from aiofile import async_open


async def read1():
    async with async_open("hello.txt", 'r') as afp:
        print(await afp.read())


async def read2():
    async with async_open("hello.txt", 'r') as afp:
        async for line in afp:
            print(line)


if __name__ == '__main__':
    asyncio.run(read1())
    #asyncio.run(read2())
    
