import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
import os
import glob
import timeit

start = timeit.default_timer()
periodictable = ["Bq", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl","Ar","K","Ca",
                 "Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr",
                 "Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd",
                 "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
                 "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",
                 "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Uub","Uut","Uuq","Uup","Uuh","Uus","Uuo"]
bondi = [0.00, 1.09, 1.40, 1.82, 2.00, 2.00, 1.70, 1.55, 1.52, 1.47, 1.54, 2.27, 1.73, 2.00, 2.10, 1.80, 1.80,
         1.75, 1.88, 2.75, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 1.63, 1.40, 1.39, 1.87, 2.00, 1.85,
         1.90, 1.85, 2.02, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 1.63, 1.72, 1.58, 1.93, 2.17,
         2.00, 2.06, 1.98, 2.16, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 1.72, 1.66, 1.55, 1.96,
         2.02, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00,
         2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00,
         2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 2.00, 1.86]


def axis_Rotation (axis, X, Y, Z, ang):
    cos = math.cos(math.radians(ang))
    sin = math.sin(math.radians(ang))
    nsin = sin * -1
    multi = []
    if axis == 'Z':
        multi = [cos, nsin, 0, sin, cos, 0, 0, 0, 1]
    elif axis == 'Y':
        multi = [cos, 0, nsin, 0, 1, 0, sin, 0, cos]
    elif axis == 'X':
        multi = [1, 0, 0, 0, cos, nsin, 0, sin, cos]
    else:
        print('the value associated to axis needs to be X, Y, or Z. Nothing else works!')
    X_new = (round((X * multi[0]) + (Y * multi[1]) + (Z * multi[2]), 7))
    Y_new = (round((X * multi[3]) + (Y * multi[4]) + (Z * multi[5]), 7))
    Z_new = (round((X * multi[6]) + (Y * multi[7]) + (Z * multi[8]), 7))
    return [X_new, Y_new, Z_new]


def rewrite(writeX, writeY, writeZ, delete):
    writeX.append(delete[0])
    writeX.pop(0)
    writeY.append(delete[1])
    writeY.pop(0)
    writeZ.append(delete[2])
    writeZ.pop(0)
    for tmp in range(len(delete)):
        delete.pop(0)


def angle_det(axis, num, x_array, y_array, z_array):
    if axis == 'Z':
        if y_array[num] == 0.0:
            angle = 0.0
        elif x_array[num] == 0.0:
            angle = 90
        else:
            angle = round(math.degrees(math.atan(y_array[num] / x_array[num])) * -1, 7)
        return angle
    elif axis == 'Y':
        if z_array[num] == 0.0:
            angle = 0.0
        elif x_array[num] == 0.0:
            angle = 90
        else:
            angle = round(math.degrees(math.atan(z_array[num] / x_array[num])) * -1, 7)
        return angle
    elif axis == 'X':
        if y_array[num] == 0.0:
            angle = 0.0
        elif z_array[num] == 0.0:
            angle = 90
        else:
            angle = round(math.degrees(math.atan(z_array[num] / y_array[num])) * -1, 7)
        return angle
    else:
        return print('the first input of this function needs to be either X, Y, or Z referring axis to rotate about')


def angle_rot(axis, num, X, Y, Z):
    angle = angle_det(axis, num, X, Y, Z)
    for i in range(len(X)):
        array = axis_Rotation(axis, X[0], Y[0], Z[0], angle)
        rewrite(X, Y, Z, array)

afiles = []
for root, dirs, files in os.walk('C:\\Python_Scripts'):
    afiles += glob.glob(os.path.join(root, '*.xyz'))

sterimol = []
file_name = []

for files in range(len(afiles)):
    file = afiles[files]
    temp = file.split('\\')
    temp = temp[2].split('.')
    file_name.append(temp[0])
    xyz = open(file).read().split()
    atoms = xyz[0::4]
    xyz = np.delete(xyz, slice(None, None, 4))
    X = xyz[0::3].astype(np.float)
    xyz = np.delete(xyz, slice(None, None, 3))
    Y = xyz[0::2].astype(np.float)
    xyz = np.delete(xyz, slice(None, None, 2))
    Z = xyz.astype(np.float)

    # Translation so the first index is the origin
    X = [round((a - X[0]), 7) for a in X]
    Y = [round((a - Y[0]), 7) for a in Y]
    Z = [round((a - Z[0]), 7) for a in Z]

    # Rotation about the Z-axis so the second atom has no Y  vector
    angle_rot('Z', 1, X, Y, Z)
    angle_rot('Y', 1, X, Y, Z)

    B_value = []
    distances = []
    for i in range(len(X)):
        for j in range(len(X)):
            distances.append((((X[i]-X[j])**2)+((Y[i]-Y[j])**2)+((Z[i]-Z[j])**2))**(1/2))
    length = distances[0:(len(X))]
    radii = []
    test = 0
    for i in atoms:
        test += 1
        for j in periodictable:
            if i ==j:
                radii.append(bondi[periodictable.index(i)])
            else:
                pass
    if len(X) <= 2:
        for atom in range(len(X)):
            B_value.append(np.max([round(abs(Y[i] - radii[i]), 3) for i in range(len(radii))]))
            B_value.append(abs(np.min([round(Y[i] - radii[i], 3) for i in range(len(radii))])))
            B_value.append(np.max([round(abs(radii[i] - Y[i]), 3) for i in range(len(radii))]))
            B_value.append(np.max([round(abs(radii[i]) + abs(Y[i]), 3) for i in range(len(radii))]))
            B_value.append(np.max([round(abs(radii[i]) + abs(Z[i]), 3) for i in range(len(radii))]))
            B_value.append(np.max([round(abs(Z[i] - radii[i]), 3) for i in range(len(radii))]))
            B_value.append(abs(np.min([round(Z[i] - radii[i], 3) for i in range(len(radii))])))
            B_value.append(np.max([round(abs(radii[i] - Z[i]), 3) for i in range(len(radii))]))
    else:
        for full in range(90):
            angle = full
            for i in range(len(X)):
                array = axis_Rotation('X', X[0], Y[0], Z[0], angle)
                rewrite(X, Y, Z, array)
            B_value.append(np.max([round(abs(Y[i] - radii[i]), 3) for i in range(len(radii))]))
            B_value.append(abs(np.min([round(Y[i] - radii[i], 3) for i in range(len(radii))])))
            B_value.append(np.max([round(abs(radii[i] - Y[i]), 3) for i in range(len(radii))]))
            B_value.append(np.max([round(abs(radii[i]) + abs(Y[i]), 3) for i in range(len(radii))]))
            B_value.append(np.max([round(abs(radii[i]) + abs(Z[i]), 3) for i in range(len(radii))]))
            B_value.append(np.max([round(abs(Z[i] - radii[i]), 3) for i in range(len(radii))]))
            B_value.append(abs(np.min([round(Z[i] - radii[i], 3) for i in range(len(radii))])))
            B_value.append(np.max([round(abs(radii[i] - Z[i]), 3) for i in range(len(radii))]))

    L_abs = round(np.max([abs(radii[i])+abs(length[i]) for i in range(len(radii))]), 3)
    L_sti = round(np.max([abs(radii[i])+abs(X[i]) for i in range(len(radii))]), 3)
    B5 = np.max(B_value)
    B1 = np.min(B_value)
    sterimol.append([L_abs, L_sti, B1, B5])

df = pd.DataFrame(sterimol, index=file_name, columns=['L_abs', 'L_sti', 'B1', 'B5'])
print(df)
df.to_csv(open('sterimol.csv', 'w'))

stop = timeit.default_timer()
print(stop - start)
