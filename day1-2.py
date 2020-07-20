# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:01:44 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

mc.player.setTilePos(100,100,100)
x=87
y=94
z=12
mc.player.setTilePos(x,y,z)