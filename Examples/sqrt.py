def heron_sqrt(number, eps, xn_1=1.0):
    xn = 0.5 * (xn_1 + number / xn_1)
    if abs(xn_1 - xn) <= eps:
        return xn
    return heron_sqrt(number, eps, xn)


print(heron_sqrt(6.25, 0.001))