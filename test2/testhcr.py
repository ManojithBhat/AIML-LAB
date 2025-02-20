def hillclimbsearch(func,start,max_iteration=1000,step_size=0.01):
    current_position = start
    current_value = func(start)

    for _ in range(max_iteration):

        next_pos_position = current_position + step_size
        next_pos_value = func(next_pos_position)

        next_neg_position = current_position - step_size
        next_neg_value = func(next_neg_position)

        if next_pos_value > current_value and next_pos_value >= next_neg_value : 
            current_position = next_pos_position
            current_value = next_pos_value
        elif next_neg_value > current_value and next_neg_value > next_pos_value:
            current_position = next_neg_position
            current_value = next_neg_value
        else : 
            break
    return current_position,current_value

#user input 
while True:
    func_val = input("Enter the function of x : ")

    try:
        x = 0
        eval(func_val)
        break #break condition is compulasary
    except:
        print("Please enter correct function of x : ")

func = lambda x : eval(func_val)

while(True):
    starting_Pos = input("please enter the starting point " )
    try:
        starting_Pos = float(starting_Pos)
        break
    except ValueError:
        print("Please enter floating point number : ")
    

position, value = hillclimbsearch(func,starting_Pos)

print(position,value)