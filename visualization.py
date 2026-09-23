# ============================================
# ROBOT VISUALIZATION AND ANIMATION
# ============================================

# ============================================
# ROBOT VISUALIZATION
# ============================================

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from mdp import (
    ROWS,
    COLS,
    START,
    GOAL,
    OBSTACLES,
    get_reward
)


def visualize(path, values, policy):

    fig, ax = plt.subplots(figsize=(8, 8))

    # -----------------------------
    # Path information
    # -----------------------------

    path_length = len(path) - 1

    total_reward = 0

    for i in range(len(path) - 1):
        current_state = path[i]
        next_state = path[i + 1]

        total_reward += get_reward(
            current_state,
            next_state
        )

    # -----------------------------
    # Grid settings
    # -----------------------------

    ax.set_xlim(-0.5, COLS - 0.5)
    ax.set_ylim(ROWS - 0.5, -0.5)

    ax.set_xticks(range(COLS))
    ax.set_yticks(range(ROWS))

    ax.grid(True)

    # -----------------------------
    # Obstacles
    # -----------------------------

    for row, col in OBSTACLES:

        rectangle = plt.Rectangle(
            (col - 0.5, row - 0.5),
            1,
            1,
            fill=True
        )

        ax.add_patch(rectangle)

        ax.text(
            col,
            row,
            "X",
            ha="center",
            va="center",
            fontsize=20
        )

    # -----------------------------
    # State Values
    # -----------------------------

    for state, value in values.items():

        if state in OBSTACLES:
            continue

        row, col = state

        ax.text(
            col,
            row + 0.30,
            f"{value:.1f}",
            ha="center",
            va="center",
            fontsize=8
        )

    # -----------------------------
    # Optimal Policy Arrows
    # -----------------------------

    arrows = {
        "UP": "↑",
        "DOWN": "↓",
        "LEFT": "←",
        "RIGHT": "→",
        "GOAL": "G"
    }

    for state, action in policy.items():

        if state in OBSTACLES:
            continue

        if state == GOAL:
            continue

        row, col = state

        ax.text(
            col,
            row - 0.15,
            arrows[action],
            ha="center",
            va="center",
            fontsize=18
        )

    # -----------------------------
    # Full Optimal Path
    # -----------------------------

    path_x = []
    path_y = []

    for row, col in path:

        path_x.append(col)
        path_y.append(row)

    ax.plot(
        path_x,
        path_y,
        linestyle="--",
        linewidth=1
    )

    # -----------------------------
    # Start
    # -----------------------------

    start_row, start_col = START

    ax.text(
        start_col,
        start_row,
        "S",
        ha="center",
        va="center",
        fontsize=18,
        fontweight="bold"
    )

    # -----------------------------
    # Goal
    # -----------------------------

    goal_row, goal_col = GOAL

    ax.text(
        goal_col,
        goal_row,
        "G",
        ha="center",
        va="center",
        fontsize=18,
        fontweight="bold"
    )

    # -----------------------------
    # Visited Path Line
    # -----------------------------

    visited_line, = ax.plot(
        [],
        [],
        linewidth=4
    )

    # -----------------------------
    # Robot
    # -----------------------------

    robot, = ax.plot(
        [],
        [],
        marker="o",
        markersize=15,
        linestyle=""
    )

    # -----------------------------
    # Information Text
    # -----------------------------

    info_text = ax.text(
        0.02,
        1.02,
        "",
        transform=ax.transAxes,
        fontsize=11
    )

    # -----------------------------
    # Goal Message
    # -----------------------------

    goal_message = ax.text(
        0.5,
        -0.08,
        "",
        transform=ax.transAxes,
        ha="center",
        fontsize=14,
        fontweight="bold"
    )

    # -----------------------------
    # Animation Update
    # -----------------------------

    def update(frame):

        row = path[frame][0]
        col = path[frame][1]

        # Move robot
        robot.set_data(
            [col],
            [row]
        )

        # Highlight visited path
        visited_x = []
        visited_y = []

        for i in range(frame + 1):

            visited_x.append(path[i][1])
            visited_y.append(path[i][0])

        visited_line.set_data(
            visited_x,
            visited_y
        )

        # Current reward
        current_reward = 0

        for i in range(frame):

            current_state = path[i]
            next_state = path[i + 1]

            current_reward += get_reward(
                current_state,
                next_state
            )

        current_position = path[frame]

        # Information
        info_text.set_text(
            f"Robot Step: {frame} / {path_length}"
            f"    Position: {current_position}"
            f"\nPath Length: {path_length}"
            f"    Total Reward: {total_reward}"
            f"    Current Reward: {current_reward}"
        )

        # Goal reached
        if current_position == GOAL:

            goal_message.set_text(
                "GOAL REACHED! Robot found the optimal path."
            )

        else:

            goal_message.set_text("")

        return (
            robot,
            visited_line,
            info_text,
            goal_message
        )

    # -----------------------------
    # Animation
    # -----------------------------

    animation = FuncAnimation(
        fig,
        update,
        frames=len(path),
        interval=700,
        repeat=False
    )

    # Prevent animation garbage collection
    fig.animation = animation

    # -----------------------------
    # Title
    # -----------------------------

    ax.set_title(
        "MDP-Based Intelligent Robot Path Finder\n"
        "Value Iteration + Optimal Policy"
    )

    plt.show()