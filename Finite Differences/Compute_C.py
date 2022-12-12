import math
def test(c):
    phi = math.pi - math.acos(1-1/c)/2
    x = c/2*(2*phi - math.sin(2 * phi))
    if x > 1:
        return True
    else:
        return False
lbound = 0.5
hbound = 1
while hbound - lbound > 1e-9:
    avg = (lbound + hbound)/2
    if test(avg):
        hbound = avg
    else:
        lbound = avg
print(avg)
