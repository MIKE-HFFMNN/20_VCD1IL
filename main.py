import matplotlib as plt
import numpy as np
import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.chart import Reference, BarChart
import scipy.integrate as integrate
import scipy.special as special
import inquirer

#Shows and defines current working directory and files
print(os.getcwd())
path = r'C:\Users\va23007122\PycharmProjects\Test'
files = list(filter(os.path.isfile, os.listdir()))
print(files)

#Definition of basic variable
g = 9.81
t = 1

#Definition of basic formulas
def normal(v):
    return v*10**2
def reaction(v):
    return v/3.6*t
def danger(v):
    return normal(v)/2
def distance(v):
    return reaction(v)+normal(v)

#User selection of road surface
roadoptions = ['concrete', 'ice', 'gravel', 'sand']
questions = [
    inquirer.List('road',
                  message="Select a road option (1, 2, 3 or 4)",
                  choices=roadoptions,
                  ),
]
answer = inquirer.prompt(questions)
print(answer)

if answer == 'concrete' or answer == 'ice':
    conditionptions = ['dry', 'wet']
    questions = [
    inquirer.List('condition',
                  message="Select a condition option (1 or 2)",
                  choices=conditionptions,
                  ),
    ]
    answer2 = inquirer.prompt(questions)
    print(answer2)

#User input velocity
v = float(input("Enter velocity in km/h: "))
print("Velocity input: ", v, " km/h")

#User input vehicle mass
m = float(input("Enter vehicle mass in kg: "))
print("Mass input: ", m, " kg")

#Access Excel file for friction values
wb = load_workbook('20_VCD1IL_CODING.xlsx')
print(wb.sheetnames)
ws = wb["Sheet1"]
print(ws['C2'].value)

#Formulas for
#Fr = µ from excel*m*g
#Wk = (m*(v**2))/2
#Wf = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)

print(f'normal: {normal(v)}')
print(f'reaction: {reaction(v)}')
print(f'danger: {danger(v)}')
print(f'distance: {distance(v)}')
