# MDP-Based Intelligent Robot Path Finder

## Introduction

This project is an intelligent robot path-finding system based on Markov Decision Process (MDP) and Value Iteration.

The robot moves in a grid environment and finds an optimal path from the Start position to the Goal while avoiding obstacles.

## Objective

The main objective of this project is to find the optimal path for a robot using MDP and Value Iteration.

## Technologies Used

- Python
- Matplotlib
- Markov Decision Process (MDP)
- Value Iteration

## Main Features

- Grid World environment
- Start and Goal positions
- Obstacles
- Rewards and penalties
- Value Iteration
- Optimal Policy
- Optimal Robot Path
- Robot Animation
- Path Length
- Total Reward
- Graphical Visualization

## How It Works

The project first creates a grid environment.

The robot can move in four directions:

- UP
- DOWN
- LEFT
- RIGHT

Each movement has a reward or penalty.

Value Iteration calculates the value of each state and finds the best action for the robot.

The robot then follows the optimal policy and reaches the goal while avoiding obstacles.

## How to Run

Open the project in VS Code.

Activate the virtual environment if required.

Then run:

```bash
.venv/bin/python main.py