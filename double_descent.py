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


def gradient_descent_polynomial_fit(training_set, degree, rate=0.000001, max_steps=250000):
    step_counter = 0
    p = Polynomial([1] * (degree+1))
    recent_losses = deque()
    continue_training = True

    while continue_training:
        for x, y in training_set:
            g = gradient(p, x, y)
            p = Polynomial([c - rate*d for c, d in zip(p.coefficients, g)])

        new_loss = loss(p, training_set)
        recent_losses.append(new_loss)
        step_counter += 1

        if len(recent_losses) > 5:
            recent_losses.popleft()

            loss_reductions = [
                recent_losses[i] - recent_losses[i+1]
                for i in range(len(recent_losses)-1)
            ]

            if step_counter % 25000 == 0:
                print("{} steps; reductions {}".format(step_counter, loss_reductions))

            if all(r < 0.0000000001 for r in loss_reductions) or step_counter >= max_steps:
                continue_training = False
                print("total steps {}".format(step_counter))

    return p


# The obvious experiment to do to reproduce the double-descent phenomenon—
# 1. Pick a complicated "true" theory.
# 2. Grab test and training datasets, where the training data isn't enough to
#    pin down the polynomial.
# 3. Use `gradient_descent_polynomial_fit` with various degrees, and
#    measure the loss for each.
# 4. Prediction: the worst results will happen at the interpolation threshold
#    equal to the number of training points; higher degrees will do better,
#    even though there's not enough training data to pin down the true
#    polynomial!!

def double_descent_experiment():
    ...


if __name__ == "__main__":
    ...
    # truth = Polynomial([-7, -2, 3, 5])
    # print(truth)
    # training_set = sample_from_polynomial(truth, 10)
    # hypothesis = gradient_descent_polynomial_fit(training_set, 3)
    # print(hypothesis)
