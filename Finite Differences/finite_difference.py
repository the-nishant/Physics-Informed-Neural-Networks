import math
import pickle
import matplotlib.pyplot as plt
class Function:
    def __init__(self, window_begin = -100, window_end = 100, step_size = 0.0001):
        self.func = []
        self.window_begin = window_begin
        self.window_end = window_end
        self.step_size = step_size
    def evaluate(self, x):
        xbegin = math.floor(self.window_begin/self.step_size)
        xend = math.floor(self.window_end/self.step_size)
        if x <= xbegin * self.step_size:
            return self.func[0] - (self.func[1] - self.func[0]) * (xbegin * self.step_size -x) / self.step_size
        elif x >= xend * self.step_size:
            return self.func[-1] + (self.func[-1] - self.func[-2]) * (x - xend * self.step_size) / self.step_size
        else:
            lx = math.floor(x / self.step_size)
            rx = (math.floor(x / self.step_size) + 1)
            return self.func[lx - xbegin] + (self.func[rx - xbegin] - self.func[lx - xbegin]) * (x-lx * self.step_size)/(rx * self.step_size -lx * self.step_size)
    def plot(self, save = False, step_size = 0):
        x = [self.window_begin + i * self.step_size for i in range(0, len(self.func))]
        fig = plt.figure(figsize=(10,5))
        plt.plot(x, self.func)
        plt.title("Finite Difference Method with step size = " + str(step_size))
        plt.show()
        if save:
            fig.savefig('Step size = ' + str(step_size) + ' Finite Difference Plot.jpg', bbox_inches='tight', dpi=150)

flag = 1
lasty = 0
C = 0.5171999214217067

def derivative(x, y = 0, step_size = 0):
    global flag
    global C
    if y > 0:
        return flag * math.sqrt((C -y)/y)
    else:
        return ((1.5 * step_size * C ** (1/2) ) ** (2/3) / step_size)
    
def finite_difference(d, yintercept, window_begin = 0, window_end = 1, step_size = 0.00001):
    f = Function(window_begin, window_end, step_size)
    y = 0
    f.func.append(0)
    cur = window_begin
    xbegin = math.floor(window_begin/step_size)
    xend = math.floor(window_end/step_size)
    c = 0
    global lasty
    global flag
    lasty = 0
    flag = 1
    for i in range(xbegin+1, xend+1):
        if y > C:
            flag = -1
            y = lasty
        else:
            lasty = y
            y += step_size * d(i * step_size - step_size/2, y)
        if i == 0:
            c = y
        f.func.append(y)
    for i in range(xbegin, xend + 1):
        f.func[i - xbegin] += (yintercept-c)
    return f

def compute_loss(step_size, save = True, plotvsx = True):
    loss = 0
    w = finite_difference(lambda x, y: derivative(x, y, step_size), 0, step_size = step_size)
    actual_func = pickle.load(open('./actual_function (x, y) pairs.pkl', 'rb'))
    xy_pairs = []
    losses = []
    for i in range(0, 1001):
        losses.append((w.evaluate(i/1000) - actual_func[i][1]) ** 2)
        loss += losses[-1]
        xy_pairs.append((i/1000, w.evaluate(i/1000)))
    loss /= 1001
    if save:
        pickle.dump(xy_pairs, open('finite difference (x, y) pairs with step-size = ' + str(step_size) + '.pkl', 'wb'))
    if plotvsx:
        fig = plt.figure(figsize=(10,5))
        x = [p[0] for p in xy_pairs]
        y = losses
        plt.plot(x, y)
        plt.title("Loss vs x for step size = " + str(step_size))
        plt.ylabel("Loss")
        fig.savefig("Loss vs x for step size = " + str(step_size) + '.jpg', bbox_inches='tight', dpi=150)
    return loss

def plot_figure(step_size):
    w = finite_difference(lambda x, y: derivative(x, y, step_size), 0, step_size = step_size)
    w.plot(save = True, step_size = step_size)

def plot_loss_vs_step_size():
    x = [i/100000 for i in range(1, 101)]
    fig = plt.figure(figsize=(10,5))
    losses = [compute_loss(step_size, save = False, plotvsx = False) for step_size in x]
    plt.plot(x, losses)
    plt.title("Loss versus Step Size")
    plt.xlabel("Step Size")
    plt.ylabel("Mean Squared Error")
    fig.savefig('Loss versus Step Size.jpg', bbox_inches='tight', dpi=150)
plot_figure(0.00001)
