import matplotlib.pyplot as plt
import math

def equation(spot, time):
    return math.cos(spot) * math.e ** (-time)

x = 0
t = 0

x_values = [0]
y_values = []

while x <= 2*math.pi:
    x += math.pi/16
    x_values.append(x)

for xn in x_values:
    y_values.append(equation(xn, t))

plt.ion()
fig = plt.figure()
ax = fig.add_subplot()
graph, = ax.plot(x_values, y_values)
plt.xlabel("Distance along rod")
plt.ylabel("Temperature Celsius")
plt.title("Temperature Distribution at simulation time " + str(t))

for t in range(0, 100):
    y_values.clear()
    for xn in x_values:
        y_values.append(equation(xn, t/15))
    # print(x_values)
    # print(y_values)
    graph.set_ydata(y_values)
    plt.title("Temperature Distribution at simulation time " + str(t) + "%")
    fig.canvas.draw()
    fig.canvas.flush_events()

