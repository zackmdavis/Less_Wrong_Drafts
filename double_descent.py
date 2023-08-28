import random

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(c * x**i for i, c in enumerate(self.coefficients))

    def __repr__(self):
        constant = str(self.coefficients[0])
        other_terms = (
            (str(c) if c != 1 else "") + "x" + p
            for c, p in zip(self.coefficients[1:], "¹²³⁴⁵⁶⁷⁸⁹") if c != 0
        )
        return (
            (constant + " + " if constant != "0" else "") +
            " + ".join(other_terms)
        )


def gradient(p, x, y):
    return [2 * x**i * (p(x) - y) for i in range(len(p.coefficients))]


def update_on_example(p, x, y, rate):
    delta = gradient(p, x, y)
    return Polynomial([c - rate*d for c, d in zip(p.coefficients, delta)])

if __name__ == "__main__":
    p = Polynomial([2, 2, 2])
    print(p)
    for _ in range(100000):
        x = random.random()
        y = x**2
        p = update_on_example(p, x, y, 0.01)
        print(p)
