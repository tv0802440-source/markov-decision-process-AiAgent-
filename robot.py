# ============================================
# ROBOT PATH
# ============================================

from mdp import (
    START,
    GOAL,
    ROWS,
    COLS,
    get_next_state
)


# ============================================
# FIND ROBOT PATH
# ============================================

def get_robot_path(policy):

    # Robot starts here
    current_state = START

    # Store path
    path = [current_state]

    # Safety limit
    max_steps = ROWS * COLS * 4

    for _ in range(max_steps):

        # Stop when goal reached
        if current_state == GOAL:

            break

        # Get best action
        action = policy[current_state]

        # Move robot
        next_state = get_next_state(
            current_state,
            action
        )

        # Safety check
        if next_state == current_state:

            print("Robot is stuck!")

            break

        # Update position
        current_state = next_state

        # Add position to path
        path.append(current_state)

    return path