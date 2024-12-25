import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
from collections import Counter



def logistic_Func(x,r):
    x = x*r*(1-x)
    return x

def Log_Map(x0,r,N):

    x_list = [x0]
    for i in range(N):
        x_new = logistic_Func(x_list[i],r)
        x_list.append(x_new)

    plt.style.use('seaborn-whitegrid')
    # plt.figure(figsize=(16, 6), facecolor='lightgray')
    plt.xlabel('The number of iterations')
    plt.ylabel('The value of x')
    plt.title(f'\nLogistic Equation \nR={r}  |  x0={x0}\n')
    plt.plot(x_list, 'o:r')
    plt.show()





def Log_Map_2(x0,r,N):

    x_list = [x0]
    for i in range(N-1):
        x_new = logistic_Func(x_list[i],r)
        x_list.append(x_new)
    return x_list[N-100:]



x0 = 0.9
N = 6000
R_list = np.linspace(2.0, 4.0, 1000)
x_select = []
R_select = []
for r in R_list:
    x_select.append(Log_Map_2(x0,r,N))
    R_select.append([r] * 100)

print(len(R_select),len(x_select))

x_select = np.array(x_select).ravel()
R_select = np.array(R_select).ravel()

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(16, 6), facecolor='lightgray')
plt.xlabel('The value of R')
plt.ylabel('The value of x')
plt.title(f'\nThe bifurcation diagram of the Logistic Equation\n\n2.0 < R < 4.0  |  x0=0.3\n')
plt.scatter(R_select, x_select, color='red', s=0.1)
plt.savefig('bifurcation_diagram.png')
plt.show()

