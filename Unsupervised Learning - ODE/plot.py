import pickle
import matplotlib.pyplot as plt
import numpy as np

d = 1

xx = np.linspace(0, d, 1001, endpoint=True)
predict_history = []
with open("result.pickle", "rb") as f:
    predict_history = pickle.load(f)
for yy, step in predict_history:
    if step % 1000 == 0:
        plt.plot(xx, yy, label=f"iter={step}")
theta = np.linspace(0, 3.50837,101, endpoint = True)
plt.plot(0.2586 * (theta - np.sin(theta)), -0.2586 * (1 - np.cos(theta)), label = "exact")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("iterations.png")
plt.show()
plt.close()