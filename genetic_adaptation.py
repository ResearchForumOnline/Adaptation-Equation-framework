from .equations import genetic_adaptation_equation

class GeneticSystem:
    def __init__(self, b1=0.5, b2=1.5, eta=0.01, alpha=0.3, beta=0.4, gamma=0.7, theta=0.1, lam=0.01):
        self.b1 = b1
        self.b2 = b2
        self.eta = eta
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.theta = theta
        self.lam = lam

    def adapt(self, x, y, Q):
        return genetic_adaptation_equation(x, y, Q, self.b1, self.b2, self.eta, self.alpha, self.beta, self.gamma, self.theta, self.lam)