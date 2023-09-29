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
    truth = Polynomial(10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    training_set = sample_from_polynomial(truth, 5)
    test_set = sample_from_polynomial(truth, 50)
    for degree in range(1, 10):
        model = polynomial_fit(training_set, degree)
        print(model)
        loss = evaluate_model(model, test_set, nn.MSELoss())
        print(degree, loss)

if __name__ == "__main__":
    double_descent_experiment()
