import pandas as pd
import numpy as np
import math
import os
import glob

file_list = []
for root, dirs, files in os.walk('C:\\Python_Scripts'):
    file_list += glob.glob(os.path.join(root, '*.xyz'))

for xx in range(len(file_list)):
    aa = file_list[xx]
    xyz = open(aa).read().split()
    atoms = xyz[0::4]
    xyz = np.delete(xyz, slice(None, None, 4))
    X = xyz[0::3].astype(np.float)
    xyz = np.delete(xyz, slice(None, None, 3))
    Y = xyz[0::2].astype(np.float)
    xyz = np.delete(xyz, slice(None, None, 2))
    Z = xyz.astype(np.float)
    X = [round((a - X[0]), 7) for a in X]
    Y = [round((a - Y[0]), 7) for a in Y]
    Z = [round((a - Z[0]), 7) for a in Z]
    if Y[1] == 0.0:
        angle = 0.0
    elif Y[1] >= 0.0:
        angle = round(math.degrees(math.atan(Y[1]/X[1])) * -1, 7)
    elif Y[1] <= 0.0:
        angle = round(math.degrees(math.atan(Y[1]/X[1])) * -1, 7)
    cosa = math.cos(math.radians(angle))
    sina = math.sin(math.radians(angle))
    nsina = sina * -1
    Xn = []
    Yn = []
    Zn = []
    for i in range(len(X)):
        a = (X[i] * cosa)+(Y[i] * nsina)+(Z[i] * 0)
        Xn.append(round(a, 7))
    for i in range(len(Y)):
        b = (X[i] * sina)+(Y[i] * cosa)+(Z[i] * 0)
        Yn.append(round(b, 7))
    for i in range(len(Z)):
        c = (X[i] * 0)+(Y[i] * 0)+(Z[i] * 1)
        Zn.append(round(c, 7))
    if Zn[1] == 0.0:
        angle = 0.0
    elif Xn[1] == 0.0:
        angle = 90
    elif Zn[1] >= 0.0:
        angle = round(math.degrees(math.atan(Zn[1]/Xn[1])) * -1, 7)
    elif Zn[1] <= 0.0:
        angle = round(math.degrees(math.atan(Zn[1]/Xn[1])) * -1, 7)
    cosa = math.cos(math.radians(angle))
    sina = math.sin(math.radians(angle))
    nsina = sina * -1
    Xf = []
    Yf = []
    Zf = []
    for i in range(len(Xn)):
        a = (Xn[i] * cosa)+(Yn[i] * 0)+(Zn[i] * nsina)
        Xf.append(round(a, 7))
    for i in range(len(Y)):
        b = (Xn[i] * 0)+(Yn[i] * 1)+(Zn[i] * 0)
        Yf.append(round(b, 7))
    for i in range(len(Z)):
        c = (Xn[i] * sina)+(Yn[i] * 0)+(Zn[i] * cosa)
        Zf.append(round(c, 7))
    df = pd.DataFrame(list(zip(Xf, Yf, Zf)), index=atoms, columns=['X', 'Y', 'Z'])
    file = aa.split('.')
    file_name = file[0] + str('.out')
    file_name = open(file_name, 'w')
    df.to_csv(file_name)
