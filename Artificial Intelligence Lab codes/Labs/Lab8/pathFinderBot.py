import random
import numpy as np


def RL_environment(current_state, action, reset):
    if(current_state == None):
        current_state = random.randint(0, 5)

    R = [[-1, 0, -1, -1, -1, -1],
         [0, -1, 0, -1, 0, -1],
         [-1, 0, -1, 0, -1, 100],
         [-1, -1, 0, -1, -1, -1],
         [-1, 0, -1, -1, -1, 100],
         [-1, -1, 0, -1, 0, 100]]

    reward = R[current_state][action]

    if reward != -1:  # valid action, update current state as action
        current_state = action

    # reset the game
    if reset == True:
        current_state = random.randint(0, 5)
        reward = -1

    return reward, current_state


def train():

    # Initial training parameters

    gamma = 0.8
    goal_state = 5
    episodes = 1000

    # set initial Q-values
    Q = np.zeros((6, 6)).astype(int)

    # Learn from environment iterations
    for i in range(episodes):
        valid_action_on_state = -1

        # Reset environment
        _, current_state = RL_environment(None, 1, True)

        # Break only when you reach the goal
        while True:
            # Choose a random action possible for the current state
            while valid_action_on_state == -1:
                possible_acton = random.randint(0, 5)

                # interact with the environment and get the inmmediate reward
                reward, _ = RL_environment(
                    current_state, possible_acton, False)
                valid_action_on_state = reward

            valid_action_on_state = -1

            # Update the Q-Table
            # Get the biggest value from each row of the Q-Table
            # This will create the Qmax for each state
            next_state = possible_acton
            qMax = Q.max(axis=1)
            Q[current_state][next_state] = reward + (gamma * qMax[next_state])
            if current_state == goal_state:
                break

            # The next state will be the action
            current_state = next_state

        print(f"Finished episode {i} restart environment")

    return Q


def test(Q):
    # Possible permuted initial states, dont't include the goal state
    possible_initial_states = np.random.permutation(5)
    print(possible_initial_states)
    goal_state = 5

    # get the biggest action for every state
    action_max = np.argmax(Q, axis=1)
    msg = ''
    for i in range(len(possible_initial_states)):
        curr_state = possible_initial_states[i]
        msg = f"Initial state room_{curr_state} actions = ["
        # Follow optimal policy from initial state on goal state
        while True:
            next_state = action_max[curr_state]
            msg += f" -> {next_state} "
            curr_state = next_state
            if curr_state == goal_state:
                msg += "]"
                print(msg)
                break

        print()


Q = train()
print(Q)
test(Q)
