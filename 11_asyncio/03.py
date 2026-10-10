import asyncio

async def task_a():
    print("A started")
    await asyncio.sleep(2)
    print("A finished")

async def task_b():
    print("B started")
    await asyncio.sleep(1)
    print("B finished")

async def main():
    a = asyncio.create_task(task_a())  #scgheduled first
    b = asyncio.create_task(task_b())  #scheduled second

    print("Both scheduled")

    await b
    print("B is done")

    await a
    print("A is done")

asyncio.run(main())