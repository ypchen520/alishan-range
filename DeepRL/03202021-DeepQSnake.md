# Snake

## RL

## Implementation

### Agent

* game
* model
* Training
  * state = get_state(game)
  * action = get_move(state)
    * model.predict()
  * reward, game_over, score = game.play_step(action)
  * new_state = get_state(game)
  * remember
  * model.train()

### Game (Pygame)

* play_step(action)
  * reward, game_over, score

### Model (PyTorch)

* linear_qnet(DQN)
* model.predict(state)
  * action
* feedforward neural network
  * input
    * state: 11 boolean values
  * output
    * action: 3 values (scores)
      * e.g., [5 , 2.7 , 0.1] -> [1, 0, 0]

### Action

* (1, 0, 0): straight*
* (0, 1, 0): right turn
* (0, 0, 1): left turn

### State

* [danger straight, danger right, danger left]
* [direction up, direction right, direction down, direction left]
* [food up, food right, food down, food left]
