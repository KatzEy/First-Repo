import math
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def search_attractors():
    number_of_iterations = 0
    found = False
    time_points = np.linspace(0,40,1001)
    while not found:
        print("imma fuck boy")
        x = random.uniform(-0.5,0.5)
        y = random.uniform(-0.5,0.5)
        # random nearby point
        xe = x + random.uniform(-0.5,0.5) /1000
        ye = y + random.uniform(-0.5,0.5) /1000

        # distance between the points
        dx = x-xe
        dy = y-ye
        d0 = math.sqrt(dx*dx + dy*dy)


        a = [random.uniform(-2,2) for i in range(12)]

        x_list = [x]
        y_list = [y]

        converging = False
        lypunov = 0
        for i in range(10000):
            xnew = a[0] + a[1]*x + a[2]*x*x + a[3]*y +a[4]*y*y + a[5]*x*y
            ynew = a[6] + a[7]*x + a[8]*x*x + a[9]*y +a[10]*y*y + a[11]*x*y

            if xnew > 1e10 or ynew > 1e10 or xnew < -1e10 or ynew < -1e10:
                converging = True
                break
            if abs(x-xnew) < 1e-10 and abs(y-ynew) < 1e-10:
                converging = True
                break
            # check if chaotic
            if i > 1000:
                xenew = a[0] + a[1] * xe + a[2] * xe * xe + a[3] * ye + a[4] * ye * ye + a[5] * xe * ye
                yenew = a[6] + a[7] * xe + a[8] * xe * xe + a[9] * ye + a[10] * ye * ye + a[11] * xe * ye

                dx = xenew - xnew
                dy = yenew - ynew
                d = math.sqrt(dx * dx + dy * dy)

                # lyapunov exponent
                lypunov += math.log(abs(d/d0))

                xe = xnew + d0*dx/d
                ye = ynew + d0*dy/d

            x = xnew
            y = ynew
            x_list.append(x)
            y_list.append(y)
        print('still not found')
        number_of_iterations += 1
        #check if chaotic behavior has been found:
        if not converging and lypunov >= 10:
            found = True
            print('found! the process took ' + str(number_of_iterations) + ' iterations')

    parameters = (x_list[0],y_list[0],a)
    def normal_plot():
        plt.style.use("dark_background")
        plt.axis("off")
        plt.scatter(x_list[100:], y_list[100:],s=0.1,c="white",linewidth=0)
        plt.scatter(x_list[0], y_list[0], s=5, c="blue", label='First Point')
        plt.scatter(x_list[-1], y_list[-1], s=5, c="red", label='Last Point')
        plt.show()
    def animate_plot():
        plt.style.use("dark_background")
        fig, ax = plt.subplots()
        ax.axis("off")
        chaos_plot, = ax.plot(x_list,y_list,'o',markersize=0.1,linewidth=0)
        def update(frame):
            x_current = x_list[0:frame-1]
            y_current = y_list[0:frame-1]

            chaos_plot.set_data(x_current, y_current)
            return chaos_plot,

        animation = FuncAnimation(fig,update,frames = len(x_list),interval=100)
        plt.show()
    normal_plot()
search_attractors()


