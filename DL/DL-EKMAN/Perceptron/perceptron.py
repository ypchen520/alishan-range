import random
import matplotlib.pyplot as plt
from . import HyperParameters

class Perceptron:
    def __init__(self):
        self.learning_rate = 0
        self.weights = []
        self.x_train = []
        self.y_train = []
        self.index_list = []
        self.color_index = 0
        
    def compute_output(self, w, x):
        z = 0.0
        for i in range(len(w)):
            z += w[i] * x[i]
        if z < 0:
            return -1
        else:
            return 1
    def show_learning(self):
        print(f'w0 = {self.weights[0]:5.2f}, w1 = {self.weights[1]:5.2f}, w2 = {self.weights[2]:5.2f}')
        if self.color_index == 0:
            plt.plot([1.0], [1.0], 'b_', markersize=12)
            plt.plot([-1.0, 1.0, -1.0], [1.0, -1.0, -1.0], 'r+', markersize=12) # draw at (-1,1), (1,-1), (-1,-1)
            plt.axis([-2, 2, -2, 2])
            plt.xlabel('x1')
            plt.ylabel('x2')
        x = [-2.0, 2.0]
        plt.show()

    def initialize(self, x_train, y_train, weights):
        self.x_train = x_train
        self.y_train = y_train
        self.weights = weights
        self.index_list = [i for i in range(len(y_train))]
        # print(self.index_list)
        # print(self.weights)

    def train(self):
        random.seed(7) # should always start with the same randomized result
        # index_list = [0, 1, 2, 3]
        all_correct = False
        while not all_correct:
            all_correct = True
            random.shuffle(self.index_list)
            for i in self.index_list:
                x = self.x_train[i]
                y = self.y_train[i]
                p_out = self.compute_output(self.weights, x)
                if y != p_out:
                    for j in range(0, len(self.weights)):
                        self.weights[j] += y * HyperParameters._LEARNING_RATE * x[j]
                    all_correct = False
                    self.show_learning()