from Perceptron import perceptron

if __name__ == "__main__":
    # x = [1, -1, 3, 10, 2]
    # w = [1, 0.2, 0.3, -0.05, 0.5]
    p = perceptron.Perceptron()
    # y = p.compute_output(x,w)
    # print(y)
    # p.train()
    x = [[1.0, -1.0, -1.0], [1.0, -1.0, 1.0], [1.0, 1.0, -1.0], [1.0, 1.0, 1.0]]
    y = [1.0, 1.0, 1.0, -1.0]
    w = [0.2, -0.6, 0.25]
    p.initialize(x, y, w)
    # p.show_learning()
    p.train()
