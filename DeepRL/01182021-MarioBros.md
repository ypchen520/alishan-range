# Reinforcement Learning (Mario Bros)

## What is reinforcement learning?

* an agent learning to interact with an environment based on feedback signals it receives from the environmen 
  * an agent
  * an environment
  * interaction (action)
  * feedback
* trial and error
* RL
  * ML, Optimal Control, Reward System, Operations Research, Classical/Operant Conditioning, Bounded Rationality
    * Engineering, Computer Science, Neuroscience, Psychology, Economics, Mathematics

## Mario Bros

* The angent
  * Mario
* The environment
  * Game level
* The action
  * Jump, duck, move forward
  * our agent has to interact with the environment. 
    * It can do so by choosing an action from **a list of potential actions** that are possible for it to take.
    * each of these actions will alter the environment and will result in a change.
* **The state**
  * Mario + action + environment = state
  * The new state that our agent observes may generate a “reward” signal
  * build a model
    * the action the agent took, 
    * the change in state, and 
    * the potential reward received from the change in state
* The reward
  * points + staying alive

## How Does it work?

* RL Needs (Agent)
  * Actions
    * The list of manipulations to the environment
      * change the environment's state
      * learn to take better actions
  * Goals
    * how we define the reward signal
    * what are good and bad actions
    * simple setup: how can one get from start to finish in a grid world
  * Senses
    * what an agent uses to observe an environment
      * e.g., computer vision techniques in a video game setting

## Sub-Elements of a RL system

* **The Policy**
  * the way our agent behaves given the current state of the environment
  * Our agent observes the state of the environment and the policy is what it has learned to do
* The Reward Signal
  * The reward signal is how we measure the success of our agent
  * Numerical measure
    * point values
  * whether or not the agent is still alive
  * the agent shapes its policy based on this feedback
  * We can think of the reward signal as an immediate indicator of if an action was good or bad.
* **The Value Function**
  * **long-term planning to maximize success at a task**
    * To model this long-term performance
  * an estimate of how likely our agent is to have **long-term success**
  * In an uncertain environment, our agent **will constantly modify their estimates of value** over many iterations
* The Optimal Model of the Environment
  * An RL system may model the environment
    * allowing an agent to predict resultant states and rewards based on actions it wishes to take directly
    * in highly complex environments it is extremely hard to build such an internal model
