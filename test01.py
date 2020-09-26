import numpy
import matplotlib.pyplot as plt

pi = numpy.pi
x_axis = numpy.arange(0, 2*pi, 0.01*pi)
y_axis_sin = numpy.sin(x_axis)
y_axis_cos = numpy.cos(x_axis)
y_axis_tan = numpy.tan(x_axis)

plt.figure(1)
plt.title("Trigonometric function")
plt.plot(x_axis, y_axis_sin, color="pink", label="sin")
plt.plot(x_axis, y_axis_cos, color="orange", label="cos")
plt.plot(x_axis, y_axis_tan, color="darkseagreen", label="tan")
plt.xticks([0, 0.5*pi, pi, 1.5*pi, 2*pi])
plt.ylim(-2, 2)
plt.hlines(0, 0, 2*pi, colors="grey", linestyles="dashed")
plt.xlabel("X")
plt.legend(loc="upper left")

if __name__ == "__main__":
    plt.show()

# Please make the third curve "darkseagreen", thank you
