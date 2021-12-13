import asyncio
from kasa import SmartPlug

async def main():
    p = SmartPlug("192.168.10.155")

    await p.update()
    print(p.alias)

    if (p.is_on):
        await p.turn_off()
    else:
        await p.turn_on()


if __name__ == "__main__":
    asyncio.run(main())