#Yanluis lebron
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#load the mincraft modules
#get the players position and store to a variable say variable in MC chat
position = mc.player.getTilePos()
mc.postToChat(position)
mc.postToChat("Your X position: " + str(position.x))
mc.postToChat("Your Y position: " + str(position.y))
mc.postToChat("Your Z position: " + str(position.z))