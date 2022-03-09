# [Deep Reinforcement Learning: Pong from Pixels](http://karpathy.github.io/2016/05/31/rl/)

* Andrej Karpathy

## Four separate factors that hold back AI

* **Compute**: Moore's Law, GPUs, ASICs
* **Data**: ImageNet
* Algorithms: backprop, CNN, LSTM
* **Infrastructure**: Linux, TCP/IP, Git, AWS, TensorFlow

### Deep Q Learning
  * Q Learning with function approximation
    * function approximator: ConvNet
* AlphaGo
  * policy gradients with Monte Carlo Tree Search (MCTS)
* multiple clever tweaks on top of old algorithms

### Learn to play most ATARI games at human level

* from pixels
* Policy Gradients (PG)
  * better than DQN: end-to-end

## Pong from Pixels

* receive an image frame (a 210x160x3 byte array)
  * 1 byte = 8 bits (0~255)
* move the paddle UP or DOWN
* reward
  * +1: if the ball went pass the opponent
  * -1: if we missed the ball
  * 0: otherwise

### Policy network

* take **the state of the game**
* decide what we should do: move UP or DOWN
* 2-layer neural network
  * takes the raw image pixels
  * produces a single number indicating **the probility** of going UP
    * every iteration, **sample from this distribution** to get the actual move

```Python
hidden_layer = np.dot(W1, x) # x: input
hidden_layer[hidden_layer<0] = 0 # ReLU
logp = np.dot(W2, hidden_layer)
p = 1.0 / (1.0 + np.exp(-logp)) # sigmoid
```

* sigmoid non-linearity at the end
  * squashes the output probability to the range [0,1]
* preprocessing
  * feed difference frames to the network
    * subtraction of current and last frame
* the credit assignment problem
  * suppose we get a +1, how can we tell what made that happen

### Supervised Learning

## Resources

* [Best RL Tutorials](https://neptune.ai/blog/best-reinforcement-learning-tutorials-examples-projects-and-courses)
* [An introduction to Reinforcement Learning](https://medium.com/free-code-camp/an-introduction-to-reinforcement-learning-4339519de419)