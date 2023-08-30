import random
from collections import deque

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(c * x**i for i, c in enumerate(self.coefficients))

    def __repr__(self):
        constant = str(self.coefficients[0])
        other_terms = (
            (str(c) if c != 1 else "") + "x" + (p if p != "¹" else "")
            for c, p in zip(self.coefficients[1:], "¹²³⁴⁵⁶⁷⁸⁹") if c != 0
        )
        return (
            (constant + " + " if constant != "0" else "") +
            " + ".join(other_terms)
        )


def random_polynomial(degree, coefficient_range=(-9,9)):
    return Polynomial([random.randint(*coefficient_range) for _ in range(degree+1)])

def sample_from_polynomial(p, n, domain=(0,10)):
    samples = []
    for _ in range(n):
        x = random.uniform(*domain)
        y = p(x)
        samples.append((x, y))
    return samples

def gradient(p, x, y):
    return [2 * x**i * (p(x) - y) for i in range(len(p.coefficients))]

def loss(p, dataset):
    total_loss = 0
    for x, y in dataset:
        total_loss += (p(x) - y)**2
    return total_loss

def update_on_example(p, x, y, rate):
    delta = gradient(p, x, y)
    return Polynomial([c - rate*d for c, d in zip(p.coefficients, delta)])

def gradient_descent_polynomial_fit(training_set, degree):
    p = Polynomial([5, 5, 5])
    previous_loss = loss(p, training_set)

    recent_losses = deque()

    continue_training = True

    while continue_training:
        for x, y in training_set:
            p = update_on_example(p, x, y, 0.0001)

        new_loss = loss(p, training_set)
        recent_losses.append(new_loss)
        if len(recent_losses) > 5:
            recent_losses.popleft()

            loss_reductions = [
                recent_losses[i] - recent_losses[i+1]
                for i in range(len(recent_losses)-1)
            ]
            if all(r < 0.00000001 for r in loss_reductions):
                continue_training = False

    return p


if __name__ == "__main__":
    truth = random_polynomial(2)
    print(truth)
    training_set = sample_from_polynomial(truth, 5)
    hypothesis = gradient_descent_polynomial_fit(training_set, 2)
    print(hypothesis)
