# ============================================
# MAIN PROGRAM
# ============================================

from value_iteration import (
    value_iteration,
    get_policy
)

from robot import get_robot_path

from visualization import visualize


# ============================================
# MAIN FUNCTION
# ============================================

def main():

    print("======================================")
    print("     MDP ROBOT PATH FINDER")
    print("======================================")

    # ----------------------------------------
    # STEP 1: VALUE ITERATION
    # ----------------------------------------

    values, iterations = value_iteration()

    print(
        f"\nValue Iteration completed "
        f"in {iterations} iterations."
    )

    # ----------------------------------------
    # STEP 2: GET OPTIMAL POLICY
    # ----------------------------------------

    policy = get_policy(values)

    print("\nOptimal Policy:")

    arrows = {
        "UP": "↑",
        "DOWN": "↓",
        "LEFT": "←",
        "RIGHT": "→",
        "GOAL": "G"
    }

    for row in range(5):

        for col in range(5):

            state = (row, col)

            if state in policy:

                action = policy[state]

                print(
                    f" {arrows[action]} ",
                    end=""
                )

            else:

                print(" X ", end="")

        print()

    # ----------------------------------------
    # STEP 3: FIND ROBOT PATH
    # ----------------------------------------

    path = get_robot_path(policy)

    print("\nRobot Path:")

    print(path)

    print(
        f"\nNumber of steps: "
        f"{len(path) - 1}"
    )

    # ----------------------------------------
    # STEP 4: SHOW VISUALIZATION
    # ----------------------------------------

    visualize(
    path,
    values,
    policy
)


# ============================================
# START PROGRAM
# ============================================

if __name__ == "__main__":
    main()