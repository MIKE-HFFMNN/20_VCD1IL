import matplotlib as plt
import matplotlib as mpl
import numpy as np
import os
import math
from openpyxl import load_workbook
import tkinter as tk
from tkinter import *

#Shows and defines current working directory and files
print(os.getcwd())
path = r'C:\Users\va23007122\PycharmProjects\Test'
files = list(filter(os.path.isfile, os.listdir()))
print(files)

#Definition of basic variables
g = 9.81

#User input velocity
root=Tk()
root.geometry("600x200")
v=0
vm=0
def inputv():
    global v
    v=int(txt_Box.get("1.0", "end-1c"))
    print("Velocity input: ", v, " kp/h")
    global vm
    vm=str(v / 3.6)
    print("Velocity input: ", vm, " m/s")
    return v
    return vm
txt_Box = Text(root, height=1, width=8)
txt_Box.pack()
attri_button=Button(root, height=1, width= 16, text="input velocity in kp/h", command=lambda: inputv())
attri_button.pack()
mainloop()

"""
#User input vehicle mass
root=Tk()
root.geometry("600x200")
m=0
def inputm():
    m=int(txt_Box.get("1.0", "end-1c"))
    print("Mass input: ", m, " kg")
txt_Box=Text(root, height= 1, width=8)
txt_Box.pack()
attri_button=Button(root, height=1, width= 16, text="input mass in kg", command=lambda: inputm())
attri_button.pack()
mainloop()
"""
#User input inclination
root=Tk()
root.geometry("600x200")
y=0
def inputy():
    y=int(txt_Box.get("1.0", "end-1c"))
    print("Inclination input: ", y, "°")
txt_Box=Text(root, height= 1, width=8)
txt_Box.pack()
attri_button=Button(root, height=1, width= 16, text="input inclination in °", command=lambda: inputy())
attri_button.pack()
mainloop()

#User selection of road surface
root = tk.Tk()
servs = ['concrete', 'ice', 'water', 'gravel', 'sand']
svar = tk.StringVar()
svar.set(servs[0])
sr = servs[0]
def _get(cur):
    sr = str(cur)
    print("Road surface input: ", sr)
drop = tk.OptionMenu(root, svar, command = _get, *servs)
drop.grid(row=2, column=1)
root.mainloop()

#User selection of road condition
root = tk.Tk()
servs = ['dry', 'wet', 'aquaplaning']
svar = tk.StringVar()
svar.set(servs[0])
sc = str(servs[0])
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

ms = [cell.value for cell in ws['C'][1:]]
md = [cell.value for cell in ws['D'][1:]]
print(ms)
print(md)

if sr == "concrete" and sc == "dry":
    rs = ms[0]
    rd = md[0]
elif sr == "concrete" and sc == "wet":
    rs = [ms[1]]
    rd = [md[1]]
elif sr == "ice" and sc == "dry":
    rs = [ms[2]]
    rd = [md[2]]
elif sr == "ice" and sc == "wet":
    rs = [ms[3]]
    rd = [md[3]]
elif sr == "water" and sc == "aquaplaning":
    rs = [ms[4]]
    rd = [md[4]]
elif sr == "gravel" and sc == "dry":
    rs = [ms[5]]
    rd = [md[5]]
elif sr == "sand" and sc == "dry":
    rs = [ms[6]]
    rd = [md[6]]
else:
    print("Failure - option not possible")
print("rs: ", rs)
print("rd: ", rd)

#Definition of basic formulas
def calcsnormal(v):
    snormal = v*10**2
    return snormal
def calcsreaction(vm):
    sreaction = vm*t
    return sreaction
def calcsdanger(v):
    sdanger = snormal(v)/2
    return sdanger
def calcdistance(v):
    distance = sreaction(v)+snormal(v)
    return distance
def calcfn(g, m):
    fn = m*g
    return fn
def calcamax(rs, g, y):
    amax = rs*g*math.cos(math.radians(y))+g*math.sin(math.radians(y))
    return amax
def calcs(vm, a):
    s = (vm^2)/(2*a)
    return s
def calctmax(rs, vm, y):
    amax = rs * g * math.cos(math.radians(y)) + g * math.sin(math.radians(y))
    return vm/amax

#call calculation of tmax
tmax = calctmax(rs, vm, y)
print(rs)
print(vm, "m/s")
print(tmax, "s")
tr = abs(math.ceil(t))
tv = np.arange(0, tr, 0.1)
sv = [None] * len(tv)
vv = [None] * len(tv)
vv[0] = vm


"""
#Doublecheck µ values
print(rs)
print(rd)
"""