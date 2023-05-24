# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:

              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """

        # print(mdp.getStates())

        
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        # Perform the value iteration while the current number of iterations is less 
        # than the required number of iterations
        for _ in range(0, self.iterations):
            # This is to keep track of our values in current iterations
            all_values = util.Counter()
            # It will return a list of possible coordinates(states) where our agent can be
            possible_states = mdp.getStates()
            # Now for each of these states figure out the maximum Q-value and storing it 
            # in our current dictionary
            for state in possible_states:
                # If its the terminal state, no need to perform the iteration
                if mdp.isTerminal(state):
                    continue
                else:   
                    # Initializing the dictionary to store the Q values possible 
                    # for current state
                    current_Q_values = util.Counter()
                    # To retrieve the possible actions from the current state
                    possible_actions = mdp.getPossibleActions(state)
                    # Now iterate over these actions and get their q-values
                    for action in possible_actions:
                        # For my current action store its q-value
                        current_Q_values[action] = self.computeQValueFromValues(state, action)
                    # So the resulant value for my current state will be maximum among these q-values
                    all_values[state] = max(current_Q_values.values())
            # Update the resultant dictionary to be returned with the best values
            self.values = all_values.copy()

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        # This will return a list of states which is possible to reach from the current state 
        # and its associated probability
        state_prob_pair=self.mdp.getTransitionStatesAndProbs(state,action)

        # Initialize the value to 0
        value=0
        # Iterate over the probablities (Transition Function) and next state
        for next_state, prob in state_prob_pair:
            # Compute q-values 
            value += prob*(self.mdp.getReward(state,action,next_state) + self.discount*self.values[next_state])

        return value


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"

        # This function will compute the best action according to the value function
        # given by self.values

        # Fetching the possible actions from the current state
        possible_actions = self.mdp.getPossibleActions(state)

        # If the current state is terminal state or there are no legel actions
        # available then return None
        if self.mdp.isTerminal(state) or len(possible_actions) == 0:
            return None
        
        # Now initialize a counter to hold our values
        values = util.Counter()
        
        # Iterate over the possible actions and compute their q-values
        for current_action in possible_actions:
            values[current_action] = self.computeQValueFromValues(state, current_action)
        
        # Returning the best action
        return values.argMax()


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
