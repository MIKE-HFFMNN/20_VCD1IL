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
ms = [0.65, 0.4, 0.2, 0.1, 0.1, 0, 0]
md = [0.5, 0.35, 0.15, 0.08, 0.05, 0.35, 0.3]

#Definition of basic formulas
def normal(v):
    return v*10**2
def reaction(v):
    return v/3.6*t
def danger(v):
    return normal(v)/2
def distance(v):
    return reaction(v)+normal(v)
"""
def Fn:
    return rs*g*m
"""

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
servs = ['concrete', 'ice', 'water', 'gravel', 'sand']
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
servs = ['dry', 'wet', 'aquaplaning']
svar = tk.StringVar()
svar.set(servs[0])
sc = servs[0]
def _get(cur):
    sc = cur
    print("Road condition input: ", sc)
drop = tk.OptionMenu(root, svar, command = _get, *servs)
drop.grid(row=2, column=1)
root.mainloop()

#Access Excel file for corresponding surface road (sr) friction values
wb = load_workbook('20_VCD1IL_CODING.xlsx', data_only=True)
print(wb.sheetnames)
ws = wb["Friction values"]

if sr == 'concrete' and sc == 'dry':
    rs = str(ws['C2'].value)
    print("rs: ", rs)
    rd = str(ws['D2'].value)
    print("rd: ", rd)
elif sr == 'concrete' and sc == 'wet':
    rs = str(ws['C3'].value)
    print("rs: ",rs)
    rd = str(ws['D3'].value)
    print("rd: ", rd)
elif sr == 'ice' and sc == 'dry':
    rs = str(ws['C4'].value)
    print("rs: ",rs)
    rd = str(ws['D4'].value)
    print("rd: ", rd)
elif sr == 'ice' and sc == 'wet':
    rs = str(ws['C5'].value)
    print("rs: ",rs)
    rd = str(ws['D5'].value)
    print("rd: ", rd)
elif sr == 'water' and sc == 'aquaplaning':
    rs = str(ws['C6'].value)
    print("rs: ",rs)
    rd = str(ws['D6'].value)
    print("rd: ", rd)
elif sr == 'gravel' and sc == 'dry':
    rs = str(ws['C7'].value)
    print("rs: ",rs)
    rd = str(ws['D7'].value)
    print("rd: ", rd)
elif sr == 'sand' and sc == 'dry':
    rs = str(ws['C8'].value)
    print("rs: ",rs)
    rd = str(ws['D8'].value)
    print("rd: ", rd)
else:
    print("Failure - option not possible")

"""
Formulas for
Fr = µ from excel*m*g
Wk = (m*(v**2))/2
Wf = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)

print(f'normal: {normal(v)}')
print(f'reaction: {reaction(v)}')
print(f'danger: {danger(v)}')
9print(f'distance: {distance(v)}')
"""
#Doublecheck µ values
print(rs)
print(rd)
