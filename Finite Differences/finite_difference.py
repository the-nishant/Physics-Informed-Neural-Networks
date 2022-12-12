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
        if x < self.window_begin:
            return self.func[0] - (self.func[1] - self.func[0]) * (self.window_begin-x) / self.step_size
        elif x >= self.window_end:
            return self.func[-1] + (self.func[-1] - self.func[-2]) * (x - self.window_end) / self.step_size
        else:
            xbegin = math.floor(self.window_begin/self.step_size)
            lx = math.floor(x / self.step_size)
            rx = (math.floor(x / self.step_size) + 1)
            return self.func[lx - xbegin] + (self.func[rx - xbegin] - self.func[lx - xbegin]) * (x-lx * self.step_size)/(rx-lx * self.step_size)
    def plot(self, save = False, step_size = 0):
        x = [self.window_begin + i * self.step_size for i in range(0, len(self.func))]
        fig = plt.figure(figsize=(10,5))
        plt.plot(x, self.func)
        plt.title("Finite Difference Method with step size = " + str(step_size))
        plt.show()
        if save:
            fig.savefig('Step size = ' + str(step_size) + ' Finite Differene Plot.jpg', bbox_inches='tight', dpi=150)

flag = 1
lasty = 0
C = 0.5171999214217067

def derivative(x, y = 0):
    global flag
    global C
    if y > 0:
        return flag * math.sqrt((C -y)/y)
    else:
        return 100 
    
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

def compute_loss(step_size):
    loss = 0
    w = finite_difference(lambda x, y: derivative(x, y), 0, step_size = step_size)
    actual_func = pickle.load(open('./actual_function (x, y) pairs.pkl', 'rb'))
    xy_pairs = []
    for i in range(0, 1001):
        loss += (w.evaluate(i/1000) - actual_func[i][1]) ** 2
        xy_pairs.append((i/1000, w.evaluate(i/1000)))
    loss /= 1001
    pickle.dump(xy_pairs, open('finite difference (x, y) pairs with step-size = ' + str(step_size) + '.pkl', 'wb'))
    return loss

def plot_figure(step_size):
    w = finite_difference(lambda x, y: derivative(x, y), 0, step_size = step_size)
    w.plot(step_size = step_size, save = True)
plot_figure(0.00001)
