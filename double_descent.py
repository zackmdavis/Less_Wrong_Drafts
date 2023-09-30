import random
from math import log

import torch
import torch.nn as nn
import torch.optim as optim

class Polynomial(nn.Module):
    def __init__(self, degree, coefficients=None):
        super().__init__()
        if coefficients is not None:
            self.coefficients = nn.Parameter(torch.tensor(coefficients), requires_grad=False)
        else:
            self.coefficients = nn.Parameter(torch.randn(degree + 1, requires_grad=True))

    def forward(self, x):
        y = sum(c * x ** i for i, c in enumerate(self.coefficients))
        return y

    def __repr__(self):
        coefficients = [c.item() for c in self.coefficients]
        constant = str(coefficients[0])
        other_terms = (
            (str(c) if c != 1 else "") + "x" + (p if p != "¹" else "")
            for c, p in zip(coefficients[1:], "¹²³⁴⁵⁶⁷⁸⁹") if c != 0
        )
        return (
            (constant + " + " if constant != "0" else "") +
            " + ".join(other_terms)
        )


def sample_from_polynomial(p, n, domain=(0,10)):
    samples = []
    for _ in range(n):
        x = random.uniform(*domain)
        y = p(x)
        samples.append((x, y.item()))
    return samples


def polynomial_fit(training_set, degree, epochs=20_000, log=False):
    criterion = nn.MSELoss()

    model = Polynomial(degree)

    optimizer = optim.Adam(model.parameters(), lr=0.02)

    for epoch in range(epochs):
        if log:
            if epoch % 1000 == 0:
                print(epoch, model.coefficients)
        for x, y in training_set:
            x_tensor = torch.tensor([x], dtype=torch.float32)
            y_tensor = torch.tensor([y], dtype=torch.float32)

            y_pred = model(x_tensor)

            loss = criterion(y_pred, y_tensor)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    return model


def evaluate_model(model, test_set, criterion):
    total_loss = 0.0
    with torch.no_grad():
        for x, y in test_set:
            x_tensor = torch.tensor([x], dtype=torch.float32)
            y_tensor = torch.tensor([y], dtype=torch.float32)

            y_pred = model(x_tensor)
            loss = criterion(y_pred, y_tensor)
            total_loss += loss.item()
    return log(total_loss)


# The obvious experiment to do to reproduce the double-descent phenomenon—
# 1. Pick a complicated "true" theory.
# 2. Grab test and training datasets, where the training data isn't enough to
#    pin down the polynomial.
# 3. Use `polynomial_fit` with various degrees, and
#    measure the loss for each.
# 4. Prediction: the worst results will happen at the interpolation threshold
#    equal to the number of training points; higher degrees will do better,
#    even though there's not enough training data to pin down the true
#    polynomial!!

def double_descent_experiment():
    # (x-1)(x-2)(x-3)(x-4)(x-5)(x-6)(x-7)(x-8)(x-9)
    truth = Polynomial(9, [-362880, 1026576, -1172700, 723680, -269325, 63273, -9450, 870, -45, 1])
    training_set = sample_from_polynomial(truth, 5, domain=(2, 8))
    test_set = sample_from_polynomial(truth, 50, domain=(2, 8))
    for degree in range(1, 10):
        model = polynomial_fit(training_set, degree)
        print(model)
        loss = evaluate_model(model, test_set, nn.MSELoss())
        print(degree, loss)

# this is actually too non-monotonic (down, then up, then down ... then up again)
# hypothesis: 20K epochs is still "early stopping"; I need to measure that I'm
# getting to zero training error?
#
# 1 15.725675000970334
# 2 15.53512980824423
# 3 15.687746837175872
# 4 16.209581895109952
# 5 16.3487153624384
# 6 16.2676895828645
# 7 16.007451103249903
# 8 16.984831728836927
# 9 22.828251261892657


if __name__ == "__main__":
    double_descent_experiment()
