import numpy as np
from .utils import delta_negative, delta_positive

def genetic_adaptation_equation(x, y, Q, b1, b2, eta, alpha, beta, gamma, theta, lam):
    return (
        b2 * np.log(b1 + eta * Q * x) * np.exp(lam * x) *
        (1 + alpha * delta_negative(x) + beta * delta_positive(x) + gamma * np.exp(-theta * Q * x**2))
    )