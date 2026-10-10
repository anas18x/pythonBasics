import asyncio

async def task_a():
    print("A started")
    await asyncio.sleep(2)
    print("A finished")

async def task_b():
    print("B started")
    await asyncio.sleep(1)
    print("B finished")

# async def main():
#     await task_a()
#     await task_b()

# asyncio.run(main())


# ### currently taska and taskb are sequencially
# ### we can run them concurrently using asyncio.gather
async def main_concurrent():
    await asyncio.gather(task_a(), task_b())

asyncio.run(main_concurrent())