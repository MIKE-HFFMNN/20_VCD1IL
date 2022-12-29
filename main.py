import matplotlib as plt
import numpy as np
import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.chart import Reference, BarChart
import scipy.integrate as integrate
import scipy.special as special
import inquirer
import tkinter as tk
from tkinter import *

#Shows and defines current working directory and files
print(os.getcwd())
path = r'C:\Users\va23007122\PycharmProjects\Test'
files = list(filter(os.path.isfile, os.listdir()))
print(files)

#Definition of basic variables
g = 9.81
t = 1

#Lookup table of friction values
myStatic = [0.65, 0.4, 0.2, 0.1, 0.1, 0, 0]
myDynamic = [0.5, 0.35, 0.15, 0.08, 0.05, 0.35, 0.3]

#Definition of basic formulas
def normal(v):
    return v*10**2
def reaction(v):
    return v/3.6*t
def danger(v):
    return normal(v)/2
def distance(v):
    return reaction(v)+normal(v)

#User input velocity
root=Tk()
def input():
    v=txt_Box.get("1.0", "end-1c")
    print("Velocity input: ", v, " kp/h")
txt_Box=Text(root, height= 1, width=8)
txt_Box.pack()
attri_button=Button(root, height=1, width= 16, text="input velocity in kp/h", command=lambda: input())
attri_button.pack()
mainloop()

#User input vehicle mass
root=Tk()
def input():
    m=txt_Box.get("1.0", "end-1c")
    print("Mass input: ", m, " kg")
txt_Box=Text(root, height= 1, width=8)
txt_Box.pack()
attri_button=Button(root, height=1, width= 16, text="input mass in kg", command=lambda: input())
attri_button.pack()
mainloop()

#User selection of road surface
root = tk.Tk()
servs = ['Concrete', 'Ice', 'Water', 'Gravel', 'Sand']
svar = tk.StringVar()
svar.set(servs[0])
sr = servs[0]
def _get(cur):
    sr = cur
    print("Road surface input: ", sr)
drop = tk.OptionMenu(root, svar, command = _get, *servs)
drop.grid(row=2, column=1)
root.mainloop()

#User selection of road condition
root = tk.Tk()
servs = ['Dry', 'Wet', 'Aquaplaning']
svar = tk.StringVar()
svar.set(servs[0])
sc = servs[0]
def _get(cur):
    sc = cur
    print("Road condition input: ", sc)
drop = tk.OptionMenu(root, svar, command = _get, *servs)
drop.grid(row=2, column=1)
root.mainloop()

"""
roadoptions = ['concrete', 'ice', 'gravel', 'sand']
questions = [
    inquirer.List('road',
                  message="Select a road option (1, 2, 3 or 4)",
                  choices=roadoptions,
                  ),
]
answer = inquirer.prompt(questions)
print(answer)
"""

#Access Excel file for corresponding surface road (sr) friction values
wb = load_workbook('20_VCD1IL_CODING.xlsx')
print(wb.sheetnames)
ws = wb["Sheet1"]
print(ws['C2'].value)
"""
if sr == 'concrete', sc == 'dry'
elif sr == 'concrete', sc == 'wet'
"""

#Formulas for
#Fr = µ from excel*m*g
#Wk = (m*(v**2))/2
#Wf = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)

#print(f'normal: {normal(v)}')
#print(f'reaction: {reaction(v)}')
#print(f'danger: {danger(v)}')
#9print(f'distance: {distance(v)}')