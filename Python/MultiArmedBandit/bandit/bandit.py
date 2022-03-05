import numpy as np
import scipy
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt


class Bandit:
    def __init__(self, num):
        self.num_machine = num
        self.probs = self.get_probs(num)
        self.trials = [0] * num
        self.wins = [0] * num

    def get_probs(self, num):
        return [0.3 + 0.05*x for x in range(num)]

    def pull(self, machine_num):
        if np.random.rand() < self.probs[machine_num]:
            return 1
        else:
            return 0

    def run(self, steps):
        for step in range(steps):
            pass
