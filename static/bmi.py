#!/usr/bin/env python
# -*- coding: utf-8 -*-

from browser import document
def calc_bmi():
    weight = float(document["weight"].value)
    height = float(document["height"].value)
    
    #bmi = str(weight/(height*height))
    bmi = weight*height
    rslt = document["result"]
    rslt.text = bmi
    
execute_btn = document["execute"]
#for i in range(5):
execute_btn.bind("click", calc_bmi)
