from potential_field_planning import potential_field_planning


def main():

    ox = [15.0, 5.0, 20.0, 25.0]  # obstacle x position list [m]
    oy = [25.0, 15.0, 26.0, 25.0]  # obstacle y position list [m]

    start = input('Please define the starting point(splitting with comma):')
    goal = input('Please define the goal:')

    start = start.split(",")
    goal = goal.split(",")

    sx = float(start[0])
    sy = float(start[1])

    gx = float(goal[0])
    gy = float(goal[1])

    _, _ = potential_field_planning(sx, sy, gx, gy, ox, oy, reso=0.5, rr=5.0)


if __name__ == "__main__":
    main()
    input("press any key")