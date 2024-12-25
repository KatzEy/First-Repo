import math
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint


def solve_ode_system(equations, initial_positions, time_points, *args):
    def system_of_ode(vector, t, *args):
        values = vector
        params = args
        return equations(*values, *params)

    positions = odeint(system_of_ode, initial_positions, time_points, args=args)
    return positions.T

def update(frame):
        x_current = x_sol[0:frame+1]
        y_current = y_sol[0:frame+1]
        z_current = z_sol[0:frame+1]

        x_current_2 = x_sol_2[0:frame + 1]
        y_current_2 = y_sol_2[0:frame + 1]
        z_current_2 = z_sol_2[0:frame + 1]


        plot_1.set_data(x_current,y_current)
        plot_1.set_3d_properties(z_current)

        plot_2.set_data(x_current_2, y_current_2)
        plot_2.set_3d_properties(z_current_2)

        return plot_1, plot_2


def Halvorsen():
    ### Equations
    def equations(x, y, z, a):
        return [
            -a * x - 4 * y - 4 * z - y * y,
            -a * y - 4 * z - 4 * x - z * z,
            -a * z - 4 * x - 4 * y - x * x
        ]


    ### parameters
    a=1.4

    ### starting positions
    position_0_1 = [round(random.uniform(-1,1),1) for i in range(3)]
    position_0_2 = [round(random.uniform(-1,1),1) for i in range(3)]
    time_points = np.linspace(0,40,1001)

    #### ODE solving
    positions_1 = solve_ode_system(equations, position_0_1, time_points, a)
    x_sol, y_sol, z_sol = positions_1
    positions_2 = solve_ode_system(equations, position_0_2, time_points, a)
    x_sol_2, y_sol_2, z_sol_2 = positions_2


    ### plotting
    plt.style.use("dark_background")
    fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
    ax.axis("off")
    plot_1, = ax.plot(x_sol,y_sol,z_sol,label = f"Initial point of 1st: {position_0_1}")
    plot_2, = ax.plot(x_sol_2,y_sol_2,z_sol_2,label = f"Initial point of 2nd:{position_0_2}")
    legend = ax.legend()
    legend.get_texts()[0].set_color('red')

    def update(frame):
        x_current = x_sol[0:frame+1]
        y_current = y_sol[0:frame+1]
        z_current = z_sol[0:frame+1]

        x_current_2 = x_sol_2[0:frame + 1]
        y_current_2 = y_sol_2[0:frame + 1]
        z_current_2 = z_sol_2[0:frame + 1]


        plot_1.set_data(x_current,y_current)
        plot_1.set_3d_properties(z_current)

        plot_2.set_data(x_current_2, y_current_2)
        plot_2.set_3d_properties(z_current_2)

        return plot_1, plot_2

    animation = FuncAnimation(fig,update,frames = len(time_points),interval=25)
    plt.show()

Halvorsen()

def Lorentz():
    ### Equations
    def equations(x, y, z, sigma,beta,rho):
        return [
            sigma*(y-x),
            x*(rho-z)-y,
            x*y-beta*z
        ]


    ### parameters
    sigma =10
    rho=28
    beta=8/3

    ### starting positions
    position_0_1 = [round(random.uniform(-1,1),1) for i in range(3)]
    #position_0_2 = [round(random.uniform(-1,1),1) for i in range(3)]
    position_0_2 = position_0_1 + np.array([0, 0.1, 0])

    time_points = np.linspace(0,40,1001)

    #### ODE solving
    positions_1 = solve_ode_system(equations, position_0_1, time_points, sigma,beta,rho)
    x_sol, y_sol, z_sol = positions_1
    positions_2 = solve_ode_system(equations, position_0_2, time_points, sigma,beta,rho)
    x_sol_2, y_sol_2, z_sol_2 = positions_2


    ### plotting
    plt.style.use("dark_background")
    fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
    ax.axis("off")
    plot_1, = ax.plot(x_sol,y_sol,z_sol,label = f"Initial point of 1st: {position_0_1}")
    plot_2, = ax.plot(x_sol_2,y_sol_2,z_sol_2,label = f"Initial point of 2nd:{position_0_2}",color = "blue")
    legend = ax.legend()
    legend.get_texts()[0].set_color('red')

    def update(frame):
        x_current = x_sol[0:frame+1]
        y_current = y_sol[0:frame+1]
        z_current = z_sol[0:frame+1]

        x_current_2 = x_sol_2[0:frame + 1]
        y_current_2 = y_sol_2[0:frame + 1]
        z_current_2 = z_sol_2[0:frame + 1]


        plot_1.set_data(x_current,y_current)
        plot_1.set_3d_properties(z_current)

        plot_2.set_data(x_current_2, y_current_2)
        plot_2.set_3d_properties(z_current_2)

        return plot_1, plot_2

    animation = FuncAnimation(fig,update,frames = len(time_points),interval=25)
    plt.show()

Lorentz()

def Rossler():
    ### Equations
    def equations(x, y, z, a,b,c):
        return [
            -y-z,
            x+a*y,
            b+z*(x-c)
        ]


    ### parameters
    a=0.3
    b=0.2
    c=5.7

    ### starting positions
    position_0_1 = [round(random.uniform(-1,1),1) for i in range(3)]
    #position_0_2 = [round(random.uniform(-1,1),1) for i in range(3)]
    position_0_2 = position_0_1 + np.array([0, 0.1, 0])

    time_points = np.linspace(0,40,2001)

    #### ODE solving
    positions_1 = solve_ode_system(equations, position_0_1, time_points, a,b,c)
    x_sol, y_sol, z_sol = positions_1
    positions_2 = solve_ode_system(equations, position_0_2, time_points,a,b,c)
    x_sol_2, y_sol_2, z_sol_2 = positions_2


    ### plotting
    plt.style.use("dark_background")
    fig, ax = plt.subplots(subplot_kw={'projection':'3d'})
    ax.axis("off")
    plot_1, = ax.plot(x_sol,y_sol,z_sol,label = f"Initial point of 1st: {position_0_1}")
    plot_2, = ax.plot(x_sol_2,y_sol_2,z_sol_2,label = f"Initial point of 2nd:{position_0_2}",color = "blue")
    legend = ax.legend()
    legend.get_texts()[0].set_color('red')

    def update(frame):
        x_current = x_sol[0:frame+1]
        y_current = y_sol[0:frame+1]
        z_current = z_sol[0:frame+1]

        x_current_2 = x_sol_2[0:frame + 1]
        y_current_2 = y_sol_2[0:frame + 1]
        z_current_2 = z_sol_2[0:frame + 1]


        plot_1.set_data(x_current,y_current)
        plot_1.set_3d_properties(z_current)

        plot_2.set_data(x_current_2, y_current_2)
        plot_2.set_3d_properties(z_current_2)

        return plot_1, plot_2

    animation = FuncAnimation(fig,update,frames = len(time_points),interval=25)
    plt.show()

Rossler()