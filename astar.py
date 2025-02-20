def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move(state, direction):
    i, j = find_blank(state)
    new_state = [row[:] for row in state]

    if direction == "UP" and i > 0:
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
    elif direction == "DOWN" and i < 2:
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
    elif direction == "LEFT" and j > 0:
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
    elif direction == "RIGHT" and j < 2:
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
    else:
        return None
    return new_state


def calculate_heuristic(state, goal_state):
    return sum(
        1
        for i in range(3)
        for j in range(3)
        if state[i][j] != goal_state[i][j] and state[i][j] != 0
    )

def a_star(initial_state, goal_state):
    OPEN = [(calculate_heuristic(initial_state, goal_state), 0, initial_state, 0)] #(h,t,initial_state,iteration)
    CLOSED = set()

    while OPEN:
        # Get the state with the lowest f value
        f, g, current_state, iteration = min(OPEN)
        OPEN.remove((f, g, current_state, iteration))
        CLOSED.add(tuple(map(tuple, current_state)))

        # Check if the goal is reached
        if current_state == goal_state:
            print(f"Solution found in {iteration} moves!")
            return

        for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
            successor = move(current_state, direction)

            # Skip invalid moves
            if successor is None:
                continue

            if tuple(map(tuple, successor)) not in CLOSED:
                h = calculate_heuristic(successor, goal_state)
                g_successor = g + 1
                f_successor = g_successor + h
                i = iteration + 1

                # Check if successor is already in OPEN
                in_open = False
                for f_value, g_value, current_state_in_open, iter_value in OPEN:
                    if current_state_in_open == successor:
                        in_open = True
                        break

                if not in_open:
                    OPEN.append((f_successor, g_successor, successor, i))

    print("No solution found.")


# Input
initial_state = []
print("Enter the initial state (3x3 matrix):")
for _ in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

goal_state = []
print("Enter the goal state (3x3 matrix):")
for _ in range(3):
    row = list(map(int, input().split()))
    goal_state.append(row)

# Run A* algorithm
a_star(initial_state, goal_state)
