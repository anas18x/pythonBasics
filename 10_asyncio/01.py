import asyncio

async def make_tea(name):
    print(f"start of {name} tea making")
    await asyncio.sleep(5)
    print(f"end of {name} tea making")

async def main():
    await asyncio.gather(
        make_tea("first"),
        make_tea("second"),
        make_tea("third")
    )

asyncio.run(main())
print("hello")