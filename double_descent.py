import random
from math import log2
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


def log_loss(p, dataset):
    # print(p)
    total = 0
    for x, y in dataset:
        # print(p, p(x), y, total)
        total += log2((p(x) - y)**2)
    return total


# XXX: broken
def gradient_descent_polynomial_fit(training_set, degree, max_steps=250000):
    step_counter = 0
    p = Polynomial([random.random()] * (degree+1))
    recent_log_losses = deque([float('inf')])
    continue_training = True

    while continue_training:
        # full batch
        g = [0 for _ in range(degree+1)]
        for x, y in training_set:
            contribution = gradient(p, x, y)
            for i, c in enumerate(contribution):
                g[i] += c

        step_size = 0.01
        new_coefficients = [c - step_size*d for c, d in zip(p.coefficients, g)]
        while log_loss(Polynomial(new_coefficients), training_set) >= recent_log_losses[-1] or any(c > 9 for c in new_coefficients):
            step_size /= 2
            new_coefficients = [c - step_size*d for c, d in zip(p.coefficients, g)]
            # XXX: broken
            if step_size < 1e-30:
                import pudb; pudb.set_trace()

        print("gradient, new coeffs", g, new_coefficients)
        p = Polynomial(new_coefficients)

        new_log_loss = log_loss(p, training_set)
        recent_log_losses.append(new_log_loss)
        step_counter += 1

        if len(recent_log_losses) > 5:
            recent_log_losses.popleft()

            recent_reductions = [
                recent_log_losses[i] - recent_log_losses[i+1]
                for i in range(len(recent_log_losses)-1)
            ]

            if step_counter % 25000 == 0:
                print("{} steps; reductions {}".format(step_counter, recent_reductions))

            if step_counter >= max_steps:
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
    truth = Polynomial([6, 5, 4, 3, 2, 1])
    training_set = sample_from_polynomial(truth, 200)
    gradient_descent_polynomial_fit(training_set, 5, max_steps=1000000)
    # truth = Polynomial([-7, -2, 3, 5])
    # print(truth)
    # training_set = sample_from_polynomial(truth, 10)
    # hypothesis = gradient_descent_polynomial_fit(training_set, 3)
    # print(hypothesis)
