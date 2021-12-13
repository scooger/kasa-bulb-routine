import asyncio
import random
from time import sleep
from kasa import SmartBulb

async def main():
  
  #Instantiate bulb object
  targetIP="192.168.10.222"
  b = SmartBulb(targetIP)
  
  #Get details 
  await b.update()
  print(b.alias)
  
  #Turn bulb on if currently off
  if (not b.is_on):
    await b.turn_on()

  #Generate random integer for colors
  randColor=random.randint(0,301)
  print("Random HUE (color): ",randColor)
  await b.set_hsv(randColor,100,80)
  
if __name__ == "__main__":
  asyncio.run(main())
