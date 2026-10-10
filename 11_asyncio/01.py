import asyncio

async def asynchronous():
    return "Hello"

async def main():
    result = await asynchronous()
    print(result)
    print("After awaiting the asynchronous function")


print("Before calling asyncio.run()")
asyncio.run(main())
print("After calling asyncio.run()")



##########################################
async def get_data():
    return "Hello"

data = asyncio.run(get_data())
print(data)