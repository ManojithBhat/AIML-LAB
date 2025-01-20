def print_state(state):
    for row in state:
        print(' '.join(map(str,row)))
print()

#finding the empty state
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j
    return 0,0

#find the heurestic value
def find_heuristic_value(current_state,goal_state):
    return sum(
        1
        for i in range(3)
        for j in range(3)
        if current_state[i][j] != goal_state[i][j] and current_state[i][j] != 0
    )


#find the next state by moving
def move(state,direction):
    i,j = find_blank(state)
    new_state = [row[:] for row in state]

    if direction == "UP" and i > 0:
        new_state[i][j],new_state[i-1][j] = new_state[i-1][j],new_state[i][j]
    elif direction=="DOWN" and i<2:
        new_state[i][j],new_state[i+1][j] = new_state[i+1][j],new_state[i][j]
    elif direction == "LEFT" and j > 0:
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1],new_state[i][j]
    elif direction == "RIGHT" and j < 2:
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1],new_state[i][j]
    else :
        return None
    return new_state

def Astar(state,goal_state):
    open = [(find_heuristic_value(state,goal_state),0,state,0)]
    close = set()

    while open:
        f,g,current_state,iteration = min(open)
        open.remove((f,g,current_state,iteration))
        close.add(tuple(map(tuple,current_state)))

        if state == goal_state:
            print(f"solution found in {iteration}")
            return
        
        for direction in ["UP","DOWN","LEFT","RIGHT"]:
            successor = move(current_state,direction)

            if successor is None:
                continue

            #check if its in the closed 
            if tuple(map(tuple,successor)) not in close:
                h = find_heuristic_value(current_state,goal_state)
                g_successor = g + 1
                f_successor = g_successor + h
                iteration = iteration + 1

                in_open = True
                #check if its not in open
                for h,g,new_state,iter in open:
                    if new_state == current_state:
                        in_open = False
                        break

                if not in_open : 
                    open.append((f_successor,g_successor,successor,iter))
    print("no solution found")

initial_state = []
for _ in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

goal_state = []
for _ in range(3):
    row = list(map(int,input().split()))
    goal_state.append(row)


Astar(initial_state,goal_state)
