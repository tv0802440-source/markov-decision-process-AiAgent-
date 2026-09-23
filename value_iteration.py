# ============================================
# VALUE ITERATION
# ============================================

# ============================================
# VALUE ITERATION
# ============================================

from mdp import (
    ROWS,
    COLS,
    GOAL,
    OBSTACLES,
    ACTIONS,
    get_next_state,
    get_reward
)


# ============================================
# VALUE ITERATION FUNCTION
# ============================================

def value_iteration(gamma=0.9, theta=0.001):

    values = {}

    # Initialize all states
    for row in range(ROWS):

        for col in range(COLS):

            state = (row, col)

            if state not in OBSTACLES:

                values[state] = 0.0

    iteration = 0

    # Value Iteration loop
    while True:

        delta = 0

        new_values = values.copy()

        # Check every state
        for state in values:

            # Goal is terminal
            if state == GOAL:

                new_values[state] = 0

                continue

            action_values = []

            # Try every action
            for action in ACTIONS:

                next_state = get_next_state(
                    state,
                    action
                )

                reward = get_reward(
                    state,
                    next_state
                )

                # Bellman Equation
                action_value = (
                    reward
                    + gamma * values[next_state]
                )

                action_values.append(action_value)

            # Best action value
            best_value = max(action_values)

            new_values[state] = best_value

            difference = abs(
                best_value - values[state]
            )

            delta = max(delta, difference)

        # Update values
        values = new_values

        iteration += 1

        # Stop when values converge
        if delta < theta:

            break

    return values, iteration


# ============================================
# GET OPTIMAL POLICY
# ============================================

def get_policy(values, gamma=0.9):

    policy = {}

    for state in values:

        # Goal
        if state == GOAL:

            policy[state] = "GOAL"

            continue

        best_action = None

        best_value = float("-inf")

        # Check every action
        for action in ACTIONS:

            next_state = get_next_state(
                state,
                action
            )

            reward = get_reward(
                state,
                next_state
            )

            action_value = (
                reward
                + gamma * values[next_state]
            )

            if action_value > best_value:

                best_value = action_value

                best_action = action

        policy[state] = best_action

    return policy