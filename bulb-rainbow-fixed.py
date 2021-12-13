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
  
  #Range settings
  hue_min = 0
  hue_max = 301
  hue_step = 10
  
  #Loop through color control
  for x in range(0,10,1):
    print("Rainbow loop: ",x)
    for i in range(hue_min, hue_max, hue_step):
        print("\tSetting bulb hue to: ",i)
        await b.set_hsv(i,100,80)
        sleep(1)

if __name__ == "__main__":
  asyncio.run(main())
