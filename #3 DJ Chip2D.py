#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 09:33:40 2022

@author: ali
"""

import glimy
render_it=1
x=glimy.Continuum(2, (230,250), 50e-9)


for i in range(4):
    x.add_energizer(glimy.DotSource((15+55*i,0), (0,1000), 10, 5.9958492e+14))

wg_len=250

for i in range(4):
    x.add(glimy.geo2D.Rectangle((9+55*i,0), (10+55*i,wg_len),10,225,1))
    x.add(glimy.geo2D.Rectangle((10+55*i,0), (10+55*i+10,wg_len),10,5,1))
    x.add(glimy.geo2D.Rectangle((20+55*i,0), (21+55*i,wg_len),10,225,1))

    x.add(glimy.geo2D.Rectangle((9+55*i+25,0), (10+55*i+25,wg_len),10,225,1))
    x.add(glimy.geo2D.Rectangle((10+55*i+25,0), (10+55*i+35,wg_len),10,5,1))
    x.add(glimy.geo2D.Rectangle((10+55*i+35,0), (11+55*i+35,wg_len),10,225,1))


for i in range(3,4):

    for j in range(4):
        x.add(glimy.geo2D.Circle((27+55*i,26+20*j), 11,11,225,1))
        x.add(glimy.geo2D.Circle((27+55*i,26+20*j), 9,7,5,1))
        x.add(glimy.geo2D.Circle((27+55*i,26+20*j), 2,6,1))
    

for i in range(4):#Modulators
    
    x.add(glimy.geo2D.Circle((52+55*i,100), 11,11,225,1))
    x.add(glimy.geo2D.Circle((52+55*i,100), 9,7,5,1))
    x.add(glimy.geo2D.Circle((52+55*i,100), 2,6,1))

for i in range(4):

    x.add(glimy.geo2D.Rectangle((21+55*i,99),(35+55*i,100),5,225))
    x.add(glimy.geo2D.Rectangle((11+55*i,100),(35+55*i,135),5,5))
    x.add(glimy.geo2D.Rectangle((21+55*i,135),(35+55*i,136),5,225))
    
    
x.add(glimy.geo2D.Rectangle((201,151), (209,159),0,5*0.7763932022500211, 0.7763932022500211))

for i in range(4):
    x.add(glimy.geo2D.Rectangle((21+55*i,184),(35+55*i,185),5,225))
    x.add(glimy.geo2D.Rectangle((11+55*i,185),(35+55*i,220),5,5))
    x.add(glimy.geo2D.Rectangle((21+55*i,220),(35+55*i,221),5,225))


    
x.view_structure(False)

if render_it:
    glimy.Render(x,1000);x.view_field()

