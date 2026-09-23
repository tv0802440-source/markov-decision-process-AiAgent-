# ============================================
# MDP ENVIRONMENT
# ============================================


# ============================================
# GRID SETTINGS
# ============================================

ROWS = 5
COLS = 5


# ============================================
# START AND GOAL
# ============================================

START = (0, 0)

GOAL = (4, 4)


# ============================================
# OBSTACLES
# ============================================

OBSTACLES = {
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 1)
}


# ============================================
# ACTIONS
# ============================================

ACTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}


# ============================================
# TRANSITION FUNCTION
# ============================================

def get_next_state(state, action):

    row, col = state

    row_change, col_change = ACTIONS[action]

    new_row = row + row_change
    new_col = col + col_change

    # Check if robot goes outside the grid
    if new_row < 0 or new_row >= ROWS:
        return state

    if new_col < 0 or new_col >= COLS:
        return state

    new_state = (new_row, new_col)

    # Check obstacle
    if new_state in OBSTACLES:
        return state

    return new_state


# ============================================
# REWARD FUNCTION
# ============================================

def get_reward(state, next_state):

    # Reaching the goal
    if next_state == GOAL:
        return 100

    # Invalid movement
    if next_state == state:
        return -10

    # Normal movement
    return -1