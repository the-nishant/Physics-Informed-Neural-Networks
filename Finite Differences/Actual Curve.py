import math
import pickle
def find_phi(x):
    C = 0.5171999214217067
    lbound = 0
    hbound = 3
    while hbound - lbound > 1e-9:
        phi = (lbound + hbound)/2
        cx = C/2 * (2 * phi - math.sin(2 * phi))
        if cx < x:
            lbound = phi
        else:
            hbound = phi
    return phi
C = 0.5171999214217067
xy_pairs = []
for i in range(0, 1001):
    x = i/1000
    phi = find_phi(x)
    y = C/2 * (1- math.cos(2 * phi))
    xy_pairs.append((x, y))
pickle.dump(xy_pairs, open('actual_function (x, y) pairs.pkl', 'wb'))
