import asyncio

async def fetch_data():
    print("Start")
    await asyncio.sleep(6)
    print("Done")
    return {"data": "fetched"}

async  def print_nums():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1=asyncio.create_task(fetch_data())
    task2=asyncio.create_task(print_nums())
    await task2
asyncio.run(main())