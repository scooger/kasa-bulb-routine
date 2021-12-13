import asyncio
from kasa import SmartBulb

async def main():
  targetIP="192.168.10.222"
  b = SmartBulb(targetIP)
  await b.update()
  print(b.alias)
  if (b.is_on):
    await b.turn_off()
  else:
    await b.turn_on()

if __name__ == "__main__":
  asyncio.run(main())
