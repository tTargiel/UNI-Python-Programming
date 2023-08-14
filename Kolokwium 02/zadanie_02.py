import random
import matplotlib.pyplot as plt

possibleMoves = ["G", "D", "P", "L"]


def generate_random_robot_path(path_length: int) -> str:
    robot_path = ""
    for i in range(0, path_length):
        robot_path += possibleMoves[random.randint(0, 3)]
    return robot_path


def robot_position_after_walk(robot_path):
    x_position = 0
    y_position = 0
    for i in robot_path:
        if i == "G":
            y_position += 1
        elif i == "D":
            y_position -= 1
        elif i == "P":
            x_position += 1
        elif i == "L":
            x_position -= 1
    return (x_position, y_position)


def plot_robot_path(robot_path):
    xpoints = [0]
    ypoints = [0]
    x_position = 0
    y_position = 0
    print(robot_path)

    for i in robot_path:
        if i == "P":
            x_position += 1
            xpoints.append(x_position)
        elif i == "L":
            x_position -= 1
            xpoints.append(x_position)
        else:
            xpoints.append(x_position)

    for j in robot_path:
        if j == "G":
            y_position += 1
            ypoints.append(y_position)
        elif j == "D":
            y_position -= 1
            ypoints.append(y_position)
        else:
            ypoints.append(y_position)

    print(xpoints, ypoints)
    plt.plot(xpoints, ypoints)
    plt.title("Rysunek trasy pokonanej przez robota")
    plt.xlabel("droga w płaszczyźnie x")
    plt.ylabel("droga w płaszczyźnie y")
    plt.show()


robot_path = generate_random_robot_path(8)
x, y = robot_position_after_walk(robot_path)
print(f"({x},{y})")
plot_robot_path(robot_path)
