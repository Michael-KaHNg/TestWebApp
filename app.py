#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:34:57 2021

@author: kang
"""

# A simple script to calculate BMI

from pywebio import STATIC_PATH

from pywebio.input import input, FLOAT
from pywebio.output import put_text
from pywebio import start_server
import argparse

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

#if __name__ == '__main__':
    #bmi()   #  run in spyder IDE
    #start_server(bmi(), port = 80  #  run on local computer through terminal

    
if __name__ == '__main__':                  #  run on cloud
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(bmi, port=args.port)
    

