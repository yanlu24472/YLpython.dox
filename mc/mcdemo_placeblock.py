#yanluis lebron
#Get the player tile position and save it to a variable
#Use the function to place a bock under your current position
#(under your y - 1)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
playerPos = mc.player.getTilePos()
mc.setBlock(playerPos.x, playerPos.y - 1, playerPos.z, 155)
