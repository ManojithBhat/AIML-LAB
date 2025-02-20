def print_state(state):
    for row in state:
        print(" ".join(map(str,row)))
    print()


def find_empty_state(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j

def move(state,dirn):
    i,j = find_empty_state(state)

    new_state = [row[:] for row in state]

    if dirn == "UP" and i > 0 :
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
    elif dirn == 'DOWN' and i < 2:
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j],new_state[i][j]
    elif dirn == "LEFT" and j > 0:
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
    elif dirn == "RIGHT" and j < 2:
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1],new_state[i][j]
    else: 
        return None
    return new_state

def heuristic(current_state,final_state):
    return sum(
        1
        for i in range(3)
        for j in range(3)
        if current_state[i][j] != final_state[i][j] and current_state[i][j] != 0
    )

def astar(state,final_state):

    OPEN = [(heuristic(state,final_state),0,state,0)]
    CLOSE = set()

    while OPEN:
        curr_f, curr_g, current_state,iter = min(OPEN)
        OPEN.remove((curr_f,curr_g,current_state,iter))
        CLOSE.add(tuple(map(tuple,current_state)))

        if current_state == final_state:
            print(f"Final state reached in {iter} iterations")
            return
        
        for dirn in ["UP","DOWN","LEFT","RIGHT"]:
            successor = move(current_state,dirn)

            if successor is None:
                continue

            if tuple(map(tuple,successor)) not in CLOSE:
                new_h = heuristic(successor,final_state)
                new_g = curr_g + 1
                new_f = new_g + new_h
                iter = iter + 1

                in_open = False
                for _ , _ , current_state_in_open, _ in OPEN:
                    if current_state_in_open == successor:
                        in_open = True
                        break

                if in_open == False:
                    OPEN.append((new_f,new_g,successor,iter))
    print("No solution found ")



initial_state = []
print("Enter the intial state ( 3* 3 )")
for _ in range(3):
    row = list(map(int,input().split()))
    initial_state.append(row)

goal_state = []
print("Enter the intial state ( 3* 3 )")
for _ in range(3):
    row = list(map(int,input().split()))
    goal_state.append(row)


astar(initial_state,goal_state)