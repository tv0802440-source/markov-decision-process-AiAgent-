from flask import Flask, render_template

from value_iteration import value_iteration, get_policy
from robot import get_robot_path


app = Flask(__name__)


@app.route("/")
def home():

    # Run Value Iteration
    values, iterations = value_iteration()

    # Generate optimal policy
    policy = get_policy(values)

    # Generate robot path
    path = get_robot_path(policy)

    return render_template(
        "index.html",
        values=values,
        policy=policy,
        path=path,
        iterations=iterations
    )


if __name__ == "__main__":
    app.run(debug=True)