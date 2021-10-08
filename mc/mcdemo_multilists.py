#Yanluis Lebron

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

multlist = [["groceries", 1], [2, 4, 9,], [1,1.5, 2]]
multlist.append(["milk","car parts","dog food"])
print(multlist[0][1])
#Make a line of wool colors
woolLine = [13, 12, 8, 7, 1]

woolGrid = [[8, 8, 8,15, 15, 15, 15, 8, 8, 8],
    [8,8,8, 15, 0, 0, 0, 0, 15,8,8,8],
[0]]

#set my position
pos = mc.player.getTilePos()
#This tile will place a line of wool
'''for i, wool in enumerate(woolLine):
    print(str(i) + " is the color " + str(wool))
    mc.setBlock(pos.x + i, pos.y, pos.z, 35, wool)'''

#this will print a GRID of wool blocks
for i, row in enumerate(woolGrid):
    print(row)
    for j, col in enumerate(row):
        print(col)
        mc.setBlock(pos.x + j, pos.y + i, pos.z, 35, col)












