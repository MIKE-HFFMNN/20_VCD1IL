import matplotlib.pyplot as plt
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

#Definition of basic variables and start values
g=9.81
v=0
vm=0
m=0
y=0

#Definition of basic formulas
def calcsnormal(v):
    snormal = float(v*10**2)
    return snormal
def calcsreaction(vm):
    sreaction = float(vm*t)
    return sreaction
def calcsdanger(v):
    sdanger = float(snormal(v)/2)
    return sdanger
def calcdistance(v):
    distance = float(sreaction(v)+snormal(v))
    return distance
def calcfn(g, m):
    fn = float(m*g)
    return fn
def calcamax(rs, g, y):
    amax = float(rs*g*math.cos(math.radians(y))+g*math.sin(math.radians(y)))
    return amax
"""
def calcs(vm, a):
    s = float((vm**2)/(2*a))
    return s
"""
def calctmax(rs, vm, y):
    amax = float(rs * g * math.cos(math.radians(y)) + g * math.sin(math.radians(y)))
    return vm/amax

#User input velocity https://realpython.com/python-gui-tkinter/
root=Tk()
root.geometry("600x200")
def inputv():
    global v
    global vm
    v=int(txt_Box.get("1.0", "end-1c"))
    while True:
        if v >= 1 and v <= 300:
            print("Velocity input: ", v, " kp/h")
            vm = float(v / 3.6)
            print("Velocity input: ", vm, " m/s")
            return v
            return vm
        else:
            error = tk.Label(text="Error - option not possible!", fg="black", width=30, height=5)
            error.pack()
            print("Error - option not possible!")
            break
greeting=tk.Label(text="Hello! Please insert velocity:",fg="black",width=30,height=5)
greeting.pack()
txt_Box=Text(root, height=1, width=8)
txt_Box.pack()
attri_button=Button(root, height=1, width= 16, text="input velocity in kp/h", command=lambda: inputv())
attri_button.pack()
mainloop()

"""
#User input vehicle mass
root=Tk()
root.geometry("600x200")
def inputm():
    m=float(txt_Box.get("1.0", "end-1c"))
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
def inputy():
    global y
    y=float(txt_Box.get("1.0", "end-1c"))
    print("Inclination input: ", y, "°")
    return y
greeting=tk.Label(text="Please insert inclination angle:",fg="black",width=30,height=5)
greeting.pack()
txt_Box=Text(root, height= 1, width=8)
txt_Box.pack()
attri_button=Button(root, height=1, width= 16, text="input inclination in °", command=lambda: inputy())
attri_button.pack()
mainloop()

#User selection of road surface https://stackoverflow.com/questions/52757496/how-to-make-tkinter-drop-down-to-save-data-in-python-3
root = tk.Tk()
root.geometry("400x200")
servs = ['concrete', 'ice', 'water', 'gravel', 'sand']
svar = tk.StringVar()
svar.set(servs[0])
sr = servs[0]
def _get(cur):
    global sr
    sr = str(cur)
    print("Road surface input: ", sr)
    return sr
drop = tk.OptionMenu(root, svar, command = _get, *servs)
drop.grid(row=2, column=1)
root.mainloop()

#User selection of road condition
root = tk.Tk()
root.geometry("400x200")
servs = ['dry', 'wet', 'aquaplaning']
svar = tk.StringVar()
svar.set(servs[0])
sc = str(servs[0])
def _get(cur):
    global sc
    sc = cur
    print("Road condition input: ", sc)
    return sc
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

def calcs(sr, sc, y, vm):
    if sr == "concrete" and sc == "dry":
        rs = float(ms[0])
        rd = float(md[0])
    elif sr == "concrete" and sc == "wet":
        rs = float(ms[1])
        rd = float(md[1])
    elif sr == "ice" and sc == "dry":
        rs = float(ms[2])
        rd = float(md[2])
    elif sr == "ice" and sc == "wet":
        rs = float(ms[3])
        rd = float(md[3])
    elif sr == "water" and sc == "aquaplaning":
        rs = float(ms[4])
        rd = float(md[4])
    elif sr == "gravel" and sc == "dry":
        rs = float(ms[5])
        rd = float(md[5])
    elif sr == "sand" and sc == "dry":
        rs = float(ms[6])
        rd = float(md[6])
    else:
        root = Tk()
        error = tk.Label(text="Error - option not possible!", fg="black", width=30, height=5)
        error.pack()
        print("Error - option not possible!")
        mainloop()
        sys.exit()

    print("rs: ", rs)
    print("rd: ", rd)

    #call calculation of tmax
    tmax = calctmax(rs, vm, y)
    print("tmax :", tmax, "s")
    tr = abs(math.ceil(tmax))
    tv = np.arange(0, tr, 0.1)
    sv = [None] * len(tv)
    vv = [None] * len(tv)
    vv[0] = vm
    print("tmax rounded-up :", tr, "s")

    #creation of vectors for plotting
    i = 0
    while i < len(tv):
        ti = tv[1] - tv[0]
        sv[i] = vm * tv[i] - 1/2 * calcamax(rs, g, y) * pow(tv[i], 2)
        vv[i+1] = vv[i] - calcamax(rs, g, y) * ti
        if vv[i] <= 0:
            break
        i += 1
    print(tv, "[s]")
    print(sv, "[m]")
    print(vv, "m/s")
    return tv, sv, vv

#call calculation of s
calcmatrix = calcs(sr, sc, y, vm)
t = calcmatrix[0]
s = calcmatrix[1]
v = calcmatrix[2]

#plotting https://stackoverflow.com/questions/14762181/adding-a-y-axis-label-to-secondary-y-axis-in-matplotlib
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(t, s, label='distance s', color='r')
ax2.plot(t, v, label='velocity v', color='k')

ax1.set_xlabel('time [s]')
ax1.set_ylabel('distance [m]')
ax2.set_ylabel('velocity [m/s]')

plt.title("velocity and distance over time")
plt.legend()
plt.show()