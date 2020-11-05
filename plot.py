import matplotlib.pyplot as plt

#line_graph

xs = [1, 2, 3, 4, 5]
ys = [x**2 for x in xs]

plt.scatter(xs, ys)
plt.show()