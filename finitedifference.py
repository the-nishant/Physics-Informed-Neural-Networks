import math
class Function:
    def __init__(self, window_begin = -100, window_end = 100, step_size = 0.0001):
        self.func = {}
        self.window_begin = -1000
        self.window_end = 1000
        self.step_size = step_size
    def evaluate(self, x):
        if x < self.window_begin:
            return self.func[self.window_begin] - (self.func[self.window_begin + step_size] - self.func[self.window_begin]) * (self.window_begin-x) / step_size
        elif x >= self.window_end:
            return self.func[self.window_end] + (self.func[self.window_end] - self.func[self.window_end-step_size]) * (x - self.window_end) / step_size
        else:
            lx = math.floor(x / self.step_size) * self.step_size
            rx = (math.floor(x / self.step_size) + 1) * self.step_size
            return self.func[lx] + (self.func[rx] - self.func[lx]) * (x-lx)/(rx-lx)
def derivative(x):
    return x
def finite_difference(d, yintercept, window_begin = -100, window_end = 100, step_size = 0.0001):
    f = Function(window_begin, window_end, step_size)
    y = 0
    f.func[window_begin] = 0
    cur = window_begin
    xbegin = math.floor(window_begin/step_size)
    xend = math.floor(window_end/step_size)
    for i in range(xbegin+1, xend+1):
        y += step_size * derivative(i * step_size - step_size/2)
        f.func[i * step_size] = y
    c = f.func[0]
    cur = window_begin
    for i in range(xbegin, xend + 1):
        f.func[i * step_size] -= c
    return f
w = finite_difference(lambda x: derivative(x), 0)
print(w.evaluate(5))
    
    
