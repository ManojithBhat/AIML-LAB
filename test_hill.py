def hill_climbing(func, start,max_iterations=1000,step_index = 0.01):
    current_position = start
    current_position_value = func(start)

    for _ in range(max_iterations):

        next_positive_position = current_position + step_index
        next_positive_position_value = func(next_positive_position)

        next_negative_position = current_position - step_index
        next_negative_position_value = func(next_negative_position)

        if next_positive_position_value > current_position_value and next_positive_position_value >= next_negative_position_value:
            current_position = next_positive_position
            current_position_value = next_positive_position_value
        elif next_negative_position_value > current_position_value and next_negative_position_value > next_positive_position_value:
            current_position = next_negative_position
            current_position_value = next_negative_position_value
        else:
            break

    return current_position,current_position_value

while True:
    func_str = input("Enter the function of x")

    #add the value of dummy x 
    try:
        x = 0
        eval(func_str)
        break
    except:
        print("please enter the correct function")
    
func = lambda x : eval(func_str)

while True:
    start = input("Please enter the starting position to start the search : ")
    try : 
        start = float(start)
        break
    except ValueError:
        print("Enter a valid number data type")


maxima, max_value = hill_climbing(func,start)

print(maxima," ",max_value)


""" sample input : -(x-2)**2 + 4 and starting pos = 0"""