# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api (MCPI must be open and in a world at
mc = Minecraft.create()
import time

count=0
while count < 30:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y - 1, pos.z, 12)
    count += 1
    time.sleep(1)