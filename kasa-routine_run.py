import asyncio
from kasa import SmartBulb

async def main():
    p = SmartBulb("192.168.10.222")

    await p.update()
    print(p.alias)

    await p.turn_off()


if __name__ == "__main__":
    asyncio.run(main())