#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:34:57 2021

@author: kang
"""

# A simple script to calculate BMI
from pywebio.input import input, FLOAT
from pywebio.output import put_text
from pywebio import start_server

def bmi():
    height = input("Input your height(cm)：", type=FLOAT)
    weight = input("Input your weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            break

if __name__ == '__main__':
    #bmi()   #  run in spyder IDE
    #start_server(bmi(), port = 80)  #  run on local computer through terminal
    start_server(bmi(), debug=True, port=8080, cdn=False)  #  run on cloud