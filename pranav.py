def print_state(state):
    for row in state:
        print(*row)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j
def move(state,direction):
    i,j=find_blank(state)
    new_state=[row[:]for row in state]
    if direction == "UP" and i > 0: new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
    elif direction == "DOWN" and i < 2: new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
    elif direction == "LEFT" and j > 0: new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
    elif direction == "RIGHT" and j < 2: new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
    else: return None   
    return new_state
def calculate_heuristic(state,goal_state):
    return sum(1 for i in range(3) for j in range(3) if state[i][j]!=goal_state[i][j] and state[i][j]!=0)
def a_star(initial_state,goal_state):
    OPEN=[(0,0,initial_state)]
    CLOSED=set()
    while OPEN:
        OPEN.sort(key =lambda x:x[0])
        f,g,current_state=OPEN.pop(0)
        CLOSED.add(tuple(map(tuple,current_state)))
        print_state(current_state)
        if current_state==goal_state:
            print("Solution found in",g,"mobes!")
            return
        for direction in["UP","DOWN","LEFT","RIGHT"]:
            successor=move(current_state,direction)
            if successor and tuple(map(tuple,successor)) not in CLOSED:
                h=calculate_heuristic(successor,goal_state)
                OPEN.append((g+h+1,g+1,successor))
    print("No solution found.")
initial_state=[list(map(int,input(f"Enter row {i+1} of initial state:").split())) for i in range(3)]
goal_state=[list(map(int,input(f"Enter row {i+1} of goal state:").split())) for i in range(3)]
a_star(initial_state,goal_state)