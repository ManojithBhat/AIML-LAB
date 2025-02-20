def minimax(node,depth,alpha,beta,isMaximising):
    if depth == 0 or isinstance(node,int):
        return node
        
    if isMaximising:
        maxEval = float("-inf")
        for child in node:
            eval = minimax(child,depth-1,alpha,beta,False)
            maxEval = max(maxEval,eval)
            alpha = max(maxEval,alpha)
            if beta <= alpha:
                break
        return maxEval
    
    else : 
        minEval = float("inf")
        for child in node:
            eval = minimax(child,depth-1,alpha,beta,True)
            minEval = min(minEval,eval)
            beta = min(beta, minEval)

            if beta <= alpha:
                break

        return minEval
    
def create_tree(flat_tree,depth):
    if depth==0:
        return flat_tree.pop(0)
    childern = []
    for _ in range(2):
        childern.append(create_tree(flat_tree,depth-1)) #send the function
    return childern

flat_tree = list(map(int,input("Please enter the value as the flat data with giving spaces : ").split(' ')))
depth = int(input("please enter the depth of the tree : "))
tree = create_tree(flat_tree,depth)

value = minimax(tree,depth,alpha=float("-inf"),beta=float("inf"),isMaximising=True)

print(value)